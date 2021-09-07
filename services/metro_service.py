from models.stop import Stop
import mongoengine

def get_stop_address(code:str):
    stop = get_stop(code)
    return stop.address

def get_stop_name(code:str):
    stop = get_stop(code)
    return stop.name

def get_stop_coords(code:str):
    stop = get_stop(code)
    return stop.location["coordinates"]

def get_itineraries(code:str):
    stop = get_stop(code)
    itineraries = [{"route": i.route.route_id ,
                   "direction" : i.direction ,
                   "color": i.route.color } for i in stop.itineraries]

    return itineraries

def get_stops():
    stops = Stop.objects()
    response = [{"code": s.code,
             "name": s.name,
             "address": s.address,
             "lat": float(s.location["coordinates"][1]),
             "lon": float(s.location["coordinates"][0]), } for s in stops]
    return response

def get_stop(code:str):
    stop = Stop.objects(code=code).first()
    return stop

#12505
    
