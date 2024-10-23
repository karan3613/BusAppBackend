

from fastapi import APIRouter, HTTPException
from Models.bus_models import BusResponse , BusStatusResponse  , BusLocationResponse , BusRouteResponse , BusLoginResponse
from Tables.bus_tables import Bus , BusRoute , BusStatus , BusLocation
from Config.dependency import db_dependency
from Serializer.bus_serializer import bus_status_serializer, bus_response_serializer, bus_login_serializer, bus_location_serializer ,bus_route_response_serializer


bus_router = APIRouter()

@bus_router.post("/register")
async def register_bus(response : BusResponse , db : db_dependency):
    db_bus = Bus(**response.model_dump())
    db.add(db_bus)
    db.commit()
    db.refresh(db_bus)
    return bus_login_serializer(db_bus)

@bus_router.get("/get/details/{bus_id}")
async def get_bus_info(bus_id : int , db : db_dependency):
    db_bus = db.query(Bus).filter(
        Bus.bus_id == bus_id
    ).first()
    if db_bus is None :
        raise HTTPException(detail= "No such bus" , status_code= 400)
    return bus_response_serializer(db_bus)


@bus_router.post("/login")
async def login_bus(response : BusLoginResponse , db : db_dependency):
    db_bus = db.query(Bus).filter(
        Bus.bus_no == response.bus_no ,
        Bus.password == response.password
    ).first()
    if db_bus is None :
        raise HTTPException(detail = "Bus Not found" , status_code= 400 )
    return bus_login_serializer(db_bus)

@bus_router.post("/status/create")
async def create_status(response : BusStatusResponse  , db : db_dependency ):
    db_status = BusStatus(**response.model_dump())
    db.add(db_status)
    db.commit()
    return

@bus_router.put("/status/update")
async def update_status(response : BusStatusResponse , db : db_dependency):
    db_status = db.query(BusStatus).filter(response.bus_id == BusStatus.bus_id).first()
    if db_status is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_status.status = response.status
    db.commit()
    db.refresh(db_status)

@bus_router.get("/status/get/{bus_id}")
async def get_status(bus_id : int , db : db_dependency):
    db_status =db.query(BusStatus).filter(bus_id == BusStatus.bus_id).first()
    if db_status is None:
        raise HTTPException(status_code=404, detail="User not found")
    return bus_status_serializer(db_status)

@bus_router.post("/routes/create")
async def register_routes(response : BusRouteResponse , db : db_dependency):
    db_routes = BusRoute(**response.model_dump())
    db.add(db_routes)
    db.commit()
    db.refresh(db_routes)

@bus_router.get("/routes/get/{bus_id}")
async def get_routes(bus_id : int  , db : db_dependency):
    db_routes = db.query(BusRoute).filter(bus_id == BusRoute.bus_id).first()
    if db_routes is None:
        raise HTTPException(status_code=404, detail="User not found")
    return bus_route_response_serializer(db_routes)


def get_shard(latitude, longitude):
    return 1


@bus_router.put("/location/update")
async def update_location(response : BusLocationResponse , db : db_dependency):
    db_location = db.query(BusLocation).filter(response.bus_id == BusLocation.bus_id).first()
    if db_location is None:
        db_location = BusLocation(**response.model_dump())
        db_location.shard_id = get_shard(response.latitude  , response.longitude)
        db.add(db_location)
        db.commit()
        return
    if response.latitude is not None :
        db_location.latitude = response.latitude
    if response.longitude is not None :
        db_location.longitude  = response.longitude
    db_location.shard_id = get_shard(response.latitude , response.longitude)
    db.commit()
    db.refresh(db_location)

@bus_router.get("location/get/{bus_id}")
async def get_location(bus_id : int , db : db_dependency):
    db_location = db.query(BusLocation).filter(bus_id == BusLocation.bus_id).first()
    if db_location is None:
        raise HTTPException(status_code=404, detail="User not found")
    return bus_location_serializer(db_location)