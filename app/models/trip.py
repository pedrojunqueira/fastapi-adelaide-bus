import mongoengine
from models.itinerary import Itinerary
from models.stop_time import StopTime


class Trip(mongoengine.Document):
    trip_id = mongoengine.IntField()
    route_id = mongoengine.StringField()
    direction_id = mongoengine.IntField()
    start_time = mongoengine.DateTimeField()
    itinerary = mongoengine.ListField(mongoengine.ReferenceField(Itinerary))
    stop_times = mongoengine.ListField(mongoengine.EmbeddedDocumentField(StopTime))
    meta = {
        "db_alias": "core",
        "collection": "trips",
    }
