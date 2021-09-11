import mongoengine


class StopTime(mongoengine.EmbeddedDocument):
    trip_id = mongoengine.IntField()
    arrival_time = mongoengine.DateTimeField()
    stop_id = mongoengine.StringField()
    stop_sequence = mongoengine.IntField()
