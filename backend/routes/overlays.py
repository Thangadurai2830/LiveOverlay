from flask import Blueprint, request, jsonify
from services.overlay_service import OverlayService
from pymongo import MongoClient
from config import Config

overlays_bp = Blueprint('overlays', __name__)

client = MongoClient(Config.MONGO_URI)
db = client.get_database()
overlay_service = OverlayService(db)

@overlays_bp.route('/overlays', methods=['POST'])
def create_overlay():
    try:
        data = request.get_json()
        overlay_id = overlay_service.create_overlay(data)
        return jsonify({'message': 'Overlay created', 'id': overlay_id}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@overlays_bp.route('/overlays', methods=['GET'])
def get_overlays():
    try:
        overlays = overlay_service.get_overlays()
        return jsonify(overlays), 200
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@overlays_bp.route('/overlays/<overlay_id>', methods=['GET'])
def get_overlay(overlay_id):
    try:
        overlay = overlay_service.get_overlay(overlay_id)
        return jsonify(overlay), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@overlays_bp.route('/overlays/<overlay_id>', methods=['PUT'])
def update_overlay(overlay_id):
    try:
        data = request.get_json()
        overlay_service.update_overlay(overlay_id, data)
        return jsonify({'message': 'Overlay updated'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@overlays_bp.route('/overlays/<overlay_id>', methods=['DELETE'])
def delete_overlay(overlay_id):
    try:
        overlay_service.delete_overlay(overlay_id)
        return jsonify({'message': 'Overlay deleted'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500