from fastapi import APIRouter, HTTPException
from Models.area_models import AreaResponse , RouteResponse , RouteBusesResponse
from Tables.area_tables import Area , Route , RouteBuses
from Config.dependency import db_dependency
from Tables.bus_tables import BusRoute, BusStatus
from Serializer.area_serializer import area_serializer, list_area_serializer , route_serializer , route_buses , list_faculty_serializer

area_router = APIRouter()


@area_router.post("/create")
async def create_area(response : AreaResponse , db :db_dependency):
    db_area = Area(**response.model_dump())
    db.add(db_area)
    db.commit()
    db.refresh(db_area)

@area_router.get("/get")
async def get_area(query : str , db : db_dependency):
    search_query = query.lower()
    # Default: Substring match (searching like a search bar)
    areas = db.query(Area).filter(Area.area_name.ilike(f"%{search_query}%")).all()
    if areas is None :
        return HTTPException(detail= "No Area Found" , status_code= 404)
    return area_serializer(areas)


@area_router.post("/route/create")
async def create_route(response : RouteResponse , db : db_dependency):
    db_route = Route(**response.model_dump())
    db.add(db_route)
    db.commit()
    db.refresh(db_route)

@area_router.get("/route/buses/{start}/{end_id}")
async def get_route_buses(start_id : int , end_id : int , db : db_dependency):
    # 1. Fetch route_id from Route table based on start_id and end_id
    route = db.query(Route).filter(
        Route.start_id == start_id,
        Route.end_id == end_id
    ).first()

    if not route:
        raise HTTPException(status_code=404, detail="Route not found")

    # 2. Fetch list of bus_ids from RouteBuses table for the route_id
    buses = db.query(RouteBuses).filter(RouteBuses.route_id == route.route_id).all()

    if not buses:
        raise HTTPException(status_code=404, detail="No buses found for this route")

    # Extract bus_ids from the list of buses
    bus_ids = [bus.bus_id for bus in buses]

    # 3. Fetch bus status from BusStatus table based on bus_ids
    statuses = db.query(BusStatus).filter(BusStatus.bus_id.in_(bus_ids)).all()

    if not statuses:
        raise HTTPException(status_code=404, detail="No bus statuses found")

    return list_faculty_serializer(statuses)
