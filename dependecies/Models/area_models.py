from pydantic import BaseModel


class RouteResponse(BaseModel):
    start_id: int
    end_id: int
    fare: int
    distance : int


class AreaResponse(BaseModel):
    area_name: str

class RouteBusesResponse(BaseModel):
    route_id: int
    bus_id: int


