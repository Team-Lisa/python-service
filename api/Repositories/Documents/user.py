import mongoengine
from mongoengine import Document


class User(Document):
    name = mongoengine.StringField()