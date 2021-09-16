import fastapi

from services import metro_service
from services.real_time import Next_services

router = fastapi.APIRouter()

@router.get("/api/get_stops")
def get_stops():
    return metro_service.get_stops()

@router.get("/api/real_time/{code}")
def real_time(code:str):
    ns = Next_services(code)
    return ns.next_services

@router.get("/api/time_table_next_n/{code}")
def time_table_next_n(code:str, n:int=1):
    response = metro_service.next_n_services(code=code, next_n=n)
    return response

@router.get("/api/track_route/{stop}/{route}")
def track_route(stop:str, route:str):
    ns = Next_services(stop)
    return ns.track_bus(route)