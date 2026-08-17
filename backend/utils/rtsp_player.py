import ffmpeg
import os
import subprocess
import threading
import time

class RTSPPlayer:
    def __init__(self):
        self.process = None
        self.is_streaming = False
        self.stream_url = None

    def start_stream(self, rtsp_url, output_dir='backend/static/streams'):
        if self.is_streaming:
            self.stop_stream()

        os.makedirs(output_dir, exist_ok=True)
        hls_path = os.path.join(output_dir, 'stream.m3u8')

        # Clean up any existing segments
        for file in os.listdir(output_dir):
            if file.endswith('.ts') or file.endswith('.m3u8'):
                os.remove(os.path.join(output_dir, file))

        # Convert RTSP to HLS using ffmpeg with optimized settings
        self.process = (
            ffmpeg
            .input(rtsp_url, rtsp_transport='tcp', buffer_size='10M')
            .output(
                hls_path,
                format='hls',
                hls_time=2,  # Smaller segments for lower latency
                hls_list_size=5,  # Keep only recent segments
                hls_flags='delete_segments+independent_segments',
                g=30,  # Keyframe interval
                sc_threshold=0,  # Disable scene change detection
                c='copy',  # Use copy mode for better performance
            )
            .overwrite_output()
            .run_async(pipe_stdout=True, pipe_stderr=True)
        )

        self.is_streaming = True
        self.stream_url = rtsp_url

        # Monitor the process in a separate thread
        threading.Thread(target=self._monitor_stream, daemon=True).start()

        # Wait a moment to ensure the stream starts
        time.sleep(2)

        return hls_path

    def stop_stream(self):
        if self.process:
            self.process.terminate()
            try:
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.process.kill()
            self.process = None
        self.is_streaming = False
        self.stream_url = None

    def _monitor_stream(self):
        while self.is_streaming and self.process:
            if self.process.poll() is not None:
                # Process has ended unexpectedly
                print("Stream process ended unexpectedly. Attempting to restart...")
                try:
                    # Try to restart the stream
                    if self.stream_url:
                        self.start_stream(self.stream_url)
                except Exception as e:
                    print(f"Failed to restart stream: {str(e)}")
                    self.is_streaming = False
                    self.stream_url = None
                break
            time.sleep(1)  # Check every second
                self.is_streaming = False
                break
            time.sleep(1)

    def get_stream_status(self):
        return {
            'is_streaming': self.is_streaming,
            'stream_url': self.stream_url
        }