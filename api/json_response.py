import fastapi

from services import metro_service
from services.real_time import Next_services

router = fastapi.APIRouter()

@router.get("/api/get_stops")
def get_stops():
    return metro_service.get_stops()

@router.get("/api/next_services/{code}")
def next_services(code:str):
    ns = Next_services(code)
    return ns.next_services
