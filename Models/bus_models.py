from pydantic import BaseModel

class BusResponse(BaseModel):
    bus_no: str
    driver_name: str
    conducter_name: str
    conducter_contact: str


class BusLocationResponse(BaseModel):
    bus_id: int
    latitude: float
    longitude: float
    shard_id: int

class BusStatusResponse(BaseModel):
    bus_id: int
    status: bool
    bus_no: str

class BusRouteResponse(BaseModel):
    bus_id: int
    stop1: int | None
    stop2: int | None
    stop3: int | None
    stop4: int | None
    stop5: int | None