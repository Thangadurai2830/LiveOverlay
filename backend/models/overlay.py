from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

class Overlay:
    def __init__(self, db):
        self.collection = db.overlays

    def create(self, data):
        data['created_at'] = datetime.utcnow()
        data['updated_at'] = datetime.utcnow()
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def get_all(self):
        return list(self.collection.find({}, {'_id': 0}))

    def get_by_id(self, overlay_id):
        return self.collection.find_one({'_id': ObjectId(overlay_id)}, {'_id': 0})

    def update(self, overlay_id, data):
        data['updated_at'] = datetime.utcnow()
        result = self.collection.update_one(
            {'_id': ObjectId(overlay_id)},
            {'$set': data}
        )
        return result.modified_count > 0

    def delete(self, overlay_id):
        result = self.collection.delete_one({'_id': ObjectId(overlay_id)})
        return result.deleted_count > 0