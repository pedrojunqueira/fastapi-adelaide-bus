import mongoengine

from models.route import Route


# Father does not know its children
class Itinerary(mongoengine.Document):
    direction = mongoengine.StringField()
    direction_id = mongoengine.IntField()
    type = mongoengine.IntField()
    route = mongoengine.ReferenceField(Route)
    meta = {
        'db_alias': 'core',
        'collection': 'itineraries',
    }
