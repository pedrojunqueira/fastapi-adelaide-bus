import fastapi
from fastapi import  Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi_chameleon.engine import template

from viewmodels.browse.stop import StopViewModel
from services import metro_service

router = fastapi.APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/stop/{code}", response_class=HTMLResponse)
def stop(request: Request, code:str):
    svm = StopViewModel(request=request, code=code)
    return templates.TemplateResponse("/browse/stop.html", svm.to_dict())


@router.get("/search")
def search(request: Request):
    return templates.TemplateResponse("/browse/search.html", {"request":request})

@router.get("/stop_test/{code}")
def stop_from_db(code: str):
    stop = metro_service.get_stop(code=code)
    return {"stop" : stop.name}