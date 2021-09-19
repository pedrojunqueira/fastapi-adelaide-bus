import mongoengine
from models.itinerary import Itinerary


# father referencing
class Stop(mongoengine.Document):
    stop_id = mongoengine.StringField()
    code = mongoengine.StringField()
    name = mongoengine.StringField()
    location = mongoengine.PointField()
    address = mongoengine.StringField()
    itineraries = mongoengine.ListField(mongoengine.ReferenceField(Itinerary))
    meta = {
        "db_alias": "core",
        "collection": "stops",
    }
