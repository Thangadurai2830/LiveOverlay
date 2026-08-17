from models.overlay import Overlay

class OverlayService:
    def __init__(self, db):
        self.overlay_model = Overlay(db)

    def create_overlay(self, data):
        required_fields = ['type', 'content', 'position', 'size']
        if not all(field in data for field in required_fields):
            raise ValueError("Missing required fields")
        return self.overlay_model.create(data)

    def get_overlays(self):
        return self.overlay_model.get_all()

    def get_overlay(self, overlay_id):
        overlay = self.overlay_model.get_by_id(overlay_id)
        if not overlay:
            raise ValueError("Overlay not found")
        return overlay

    def update_overlay(self, overlay_id, data):
        if not self.overlay_model.update(overlay_id, data):
            raise ValueError("Overlay not found or no changes made")
        return True

    def delete_overlay(self, overlay_id):
        if not self.overlay_model.delete(overlay_id):
            raise ValueError("Overlay not found")
        return True