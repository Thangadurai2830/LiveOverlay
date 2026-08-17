from flask import Flask, send_from_directory
from flask_cors import CORS
from config import Config
from routes.overlays import overlays_bp
from routes.livestream import livestream_bp
import os

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

# Register blueprints
app.register_blueprint(overlays_bp, url_prefix='/api')
app.register_blueprint(livestream_bp, url_prefix='/api')

# Serve HLS streams
@app.route('/static/streams/<path:filename>')
def serve_stream(filename):
    return send_from_directory(os.path.join(app.root_path, 'static', 'streams'), filename)

if __name__ == '__main__':
    app.run(debug=True)