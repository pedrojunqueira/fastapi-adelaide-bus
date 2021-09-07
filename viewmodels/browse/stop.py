
from services import metro_service
from starlette.requests import Request
from viewmodels.shared.viewmodel import ViewModelBase


class StopViewModel(ViewModelBase):
    def __init__(self, code: str, request: Request):
        super().__init__(request)

        self.code = code
        self.name = metro_service.get_stop_name(code)
        self.address = metro_service.get_stop_address(code)
        self.coords = metro_service.get_stop_coords(code)
        self.itineraries = metro_service.get_itineraries(code)
