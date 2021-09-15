from services.real_time import Next_services
import fastapi
from fastapi import  Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi_chameleon.engine import template

from viewmodels.browse.stop import StopViewModel
from viewmodels.browse.track import TrackViewModel
from services import metro_service

router = fastapi.APIRouter()

templates = Jinja2Templates(directory="templates")



@router.get("/", include_in_schema=False)
def index(request: Request):
    return templates.TemplateResponse("/browse/index.html", {"request":request})


@router.get("/search", include_in_schema=False)
def search(request: Request):
    return templates.TemplateResponse("/browse/search.html", {"request":request})


@router.get("/stop/{code}", response_class=HTMLResponse, include_in_schema=False)
def stop(request: Request, code:str):
    svm = StopViewModel(request=request, code=code)
    return templates.TemplateResponse("/browse/stop.html", svm.to_dict())


@router.get("/stop/tracking/{code}/{route}", include_in_schema=False)
def search(request: Request, code:str, route:str):
    tvm = TrackViewModel(request=request, code=code, route=route)
    return templates.TemplateResponse("/browse/track_bus.html", tvm.to_dict())
