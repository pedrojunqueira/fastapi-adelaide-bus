from datetime import datetime, timedelta

import mongoengine
from mongoengine.queryset.visitor import Q
from models.stop import Stop
from models.trip import Trip


def get_stop_address(code: str):
    stop = get_stop(code)
    return stop.address


def get_stop_name(code: str):
    stop = get_stop(code)
    return stop.name


def get_stop_coords(code: str):
    stop = get_stop(code)
    return stop.location["coordinates"]


def get_itineraries(code: str):
    stop = get_stop(code)
    itineraries = [
        {"route": i.route.route_id, "direction": i.direction, "color": i.route.color}
        for i in stop.itineraries
    ]

    return itineraries


def get_stops():
    stops = Stop.objects()
    response = [
        {
            "code": s.code,
            "name": s.name,
            "address": s.address,
            "lat": float(s.location["coordinates"][1]),
            "lon": float(s.location["coordinates"][0]),
        }
        for s in stops
    ]
    return response

def search_stops_top(search_str:str, top:int =100):
    stops = Stop.objects(Q(name__icontains=search_str) | Q(address__icontains=search_str))
    response = [
        {
            "code": s.code,
            "name": s.name,
            "address": s.address,
            "lat": float(s.location["coordinates"][1]),
            "lon": float(s.location["coordinates"][0]),
        }
        for s in stops
    ]
    return response[:top]


def get_stop(code: str):
    stop = Stop.objects(code=code).first()
    return stop


def arrives_in(arrival_time: datetime):
    now = datetime.now()
    at = arrival_time
    here_in = int((at - now).seconds / 60)
    return f"{here_in} min" if here_in > 1 else "now"


def next_n_services(code: str, next_n: int = 3):
    stop = Stop.objects(code=code).first()
    itns = stop.itineraries
    response = []
    for i in itns:
        itinerary = dict()
        next_services = list()
        now = datetime.now()

        trips = Trip.objects(itinerary=i)

        if trips:
            for trip in trips:
                stop_times = dict()
                # filter the times of the trip from now to 1 hour
                stp = [
                    st
                    for st in trip.stop_times
                    if (st.stop_id == stop.stop_id)
                    and (st.arrival_time.time() > now.time())
                    and (st.arrival_time.time() < (now + timedelta(hours=1)).time())
                ]
                if stp:
                    stop_times["trip_id"] = stp[0].trip_id
                    stop_times["arrival_time"] = stp[0].arrival_time
                    stop_times["arrives_in"] = arrives_in(stp[0].arrival_time)
                    stop_times["stop_id"] = stp[0].stop_id
                    next_services.append(stop_times)
        itinerary["route"] = i.route.route_id
        itinerary["color"] = i.route.color
        itinerary["direction"] = i.direction
        itinerary["next_services"] = next_services[:next_n]
        response.append(itinerary)
    return response


# 12505
