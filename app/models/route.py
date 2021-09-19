import mongoengine


# user father referencing a father does not know his child
class Route(mongoengine.Document):
    name = mongoengine.StringField()
    route_id = mongoengine.StringField()
    description = mongoengine.StringField()
    color = mongoengine.StringField()

    meta = {
        "db_alias": "core",
        "collection": "routes",
    }
