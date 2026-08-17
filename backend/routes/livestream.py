from flask import Blueprint, request, jsonify
from utils.rtsp_player import RTSPPlayer

livestream_bp = Blueprint('livestream', __name__)

rtsp_player = RTSPPlayer()

@livestream_bp.route('/stream/start', methods=['POST'])
def start_stream():
    try:
        data = request.get_json()
        rtsp_url = data.get('rtsp_url')
        if not rtsp_url:
            return jsonify({'error': 'RTSP URL is required'}), 400

        hls_path = rtsp_player.start_stream(rtsp_url)
        return jsonify({
            'message': 'Stream started',
            'hls_url': '/static/streams/stream.m3u8'
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@livestream_bp.route('/stream/stop', methods=['POST'])
def stop_stream():
    try:
        rtsp_player.stop_stream()
        return jsonify({'message': 'Stream stopped'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@livestream_bp.route('/stream/status', methods=['GET'])
def get_stream_status():
    try:
        status = rtsp_player.get_stream_status()
        return jsonify(status), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500