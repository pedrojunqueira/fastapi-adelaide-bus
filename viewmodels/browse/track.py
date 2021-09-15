from services.real_time import Next_services
from services import metro_service
from starlette.requests import Request
from viewmodels.shared.viewmodel import ViewModelBase


class TrackViewModel(ViewModelBase):
    def __init__(self, code: str, route:str, request: Request):
        super().__init__(request)

        self.code = code
        self.name = metro_service.get_stop_name(code)
        self.address = metro_service.get_stop_address(code)
        self.stop_coords = metro_service.get_stop_coords(code)
        self.route = route
        self.track_data = Next_services(code).track_bus(route)
        