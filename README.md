# RTSP Live Stream Viewer with Overlays

A modern web application for viewing RTSP live streams with customizable overlays. The application features a sleek, glassmorphic design and offers intuitive controls for managing video streams and overlays.

## Features

- 🎥 RTSP Stream Playback
- 🎨 Custom Overlay Support (Text & Images)
- 🎯 Drag & Drop Overlay Positioning
- 🎬 Real-time Overlay Editing
- 💎 Modern Glassmorphic UI
- 🌓 Smooth Animations
- 📱 Responsive Design

## Tech Stack

- **Frontend**:

  - React 18
  - Material-UI v5
  - Framer Motion
  - HLS.js
  - Axios
  - React Router

- **Backend**:
  - Flask
  - Flask-CORS
  - MongoDB
  - FFmpeg

## Prerequisites

- Python 3.8+
- Node.js 16+
- MongoDB
- FFmpeg

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:

   ```bash
   cd backend
   ```

2. Create a Python virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Unix/MacOS:
     ```bash
     source venv/bin/activate
     ```

4. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the Flask server:
   ```bash
   python -m flask run
   ```

### Frontend Setup

1. Navigate to the frontend directory:

   ```bash
   cd frontend
   ```

2. Install Node.js dependencies:

   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

The application will be available at `http://localhost:3000`.

## Usage Guide

### Streaming Video

1. Enter an RTSP URL in the input field
2. Click "Start Stream" to begin playback
3. Use the video player controls for playback control

### Managing Overlays

1. Click "Edit Overlays" to enter editing mode
2. Use the Overlay Editor panel to:
   - Add text or image overlays
   - Set overlay position and size
   - Customize text color and font size
3. Drag overlays to reposition them
4. Click the delete button (×) to remove an overlay

## API Documentation

### Endpoints

#### Stream Management

- `GET /api/stream/status` - Get current stream status
- `POST /api/stream/start` - Start streaming from RTSP URL
- `POST /api/stream/stop` - Stop current stream

#### Overlay Management

- `GET /api/overlays` - List all overlays
- `POST /api/overlays` - Create new overlay
- `PUT /api/overlays/<id>` - Update overlay
- `DELETE /api/overlays/<id>` - Delete overlay

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

### Frontend

- **React**: User interface framework
- **HLS.js**: HLS video playback in browsers
- **Axios**: HTTP client for API calls
- **CSS**: Styling

## Prerequisites

- Python 3.7+
- Node.js 14+
- MongoDB
- FFmpeg

## Installation

### Backend Setup

1. Navigate to the backend directory:

   ```bash
   cd backend
   ```

2. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure MongoDB is running on your system.

4. Configure environment variables (optional):
   - `MONGO_URI`: MongoDB connection string (default: `mongodb://localhost:27017/rtsp_app`)
   - `SECRET_KEY`: Flask secret key

### Frontend Setup

1. Navigate to the frontend directory:

   ```bash
   cd frontend
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

## Usage

### Starting the Application

1. Start the backend server:

   ```bash
   cd backend
   python app.py
   ```

   The backend will run on `http://localhost:5000`

2. Start the frontend development server:
   ```bash
   cd frontend
   npm start
   ```
   The frontend will run on `http://localhost:3000`

### Using the Application

1. **Enter RTSP URL**: Input your RTSP stream URL in the text field and click "Start Stream".

2. **Add Overlays**:

   - Choose overlay type (Text or Image)
   - For text overlays: Enter text, select color, and adjust font size
   - For image overlays: Provide image URL
   - Set position (X, Y coordinates) and size (width, height)
   - Click "Add Overlay"

3. **Edit Overlays**:

   - Click "Edit Overlays" to enter edit mode
   - Drag overlays to reposition them
   - Click the × button to delete overlays

4. **Video Controls**:
   - Use the built-in video controls for play/pause and volume adjustment

## API Documentation

See [API_DOCUMENTATION.md](API_DOCUMENTATION.md) for detailed API endpoint information.

## Project Structure

```
rtsp-livestream-app/
│
├── backend/                  # Flask backend
│   ├── app.py                # Main Flask app
│   ├── config.py             # Configuration
│   ├── requirements.txt      # Python dependencies
│   ├── models/               # MongoDB models
│   │   └── overlay.py        # Overlay schema
│   ├── routes/               # Flask API endpoints
│   │   ├── overlays.py       # CRUD API for overlays
│   │   └── livestream.py     # Livestream control
│   ├── services/             # Business logic
│   │   └── overlay_service.py
│   └── utils/                # Utilities
│       └── rtsp_player.py    # RTSP to HLS converter
│
├── frontend/                 # React frontend
│   ├── public/               # Static files
│   ├── src/
│   │   ├── App.js            # Main React component
│   │   ├── index.js          # Entry point
│   │   ├── api/              # API calls
│   │   │   └── overlayApi.js
│   │   ├── components/       # Reusable UI components
│   │   │   ├── VideoPlayer.js
│   │   │   ├── Overlay.js
│   │   │   └── OverlayEditor.js
│   │   ├── pages/            # App pages
│   │   │   └── LandingPage.js
│   │   ├── context/          # React context
│   │   │   └── OverlayContext.js
│   │   ├── hooks/            # Custom hooks
│   │   │   └── useOverlays.js
│   │   ├── styles/           # CSS files
│   │   │   └── App.css
│   │   └── utils/            # Helper functions
│   │       └── videoUtils.js
│   └── package.json
│
├── .gitignore
├── API_DOCUMENTATION.md
└── README.md
```

## Development

### Adding New Features

1. **Backend**: Add new routes in the `routes/` directory and update the main `app.py`
2. **Frontend**: Add new components in the `components/` directory and update pages accordingly

### Testing RTSP Streams

For testing purposes, you can use public RTSP streams or create temporary streams using services like:

- RTSP.me
- RTSP Stream

Example RTSP URL: `rtsp://rtsp.stream/pattern`

## Troubleshooting

### Common Issues

1. **FFmpeg not found**: Ensure FFmpeg is installed and accessible in your PATH
2. **MongoDB connection error**: Make sure MongoDB is running and the connection string is correct
3. **CORS errors**: The backend has CORS enabled, but check if your browser is blocking requests
4. **Video not playing**: Ensure the RTSP URL is accessible and FFmpeg can process it

### Logs

- Backend logs are printed to the console
- Check browser developer tools for frontend errors

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For issues or questions, please create an issue in the GitHub repository.
