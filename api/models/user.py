import mongoengine
from mongoengine import Document


class User(Document):
    name = mongoengine.StringField()

    def to_json(self):
        result = self.to_mongo().to_dict()
        if "_id" in result:
            del result["_id"]
        return result