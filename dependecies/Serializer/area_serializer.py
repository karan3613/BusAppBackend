from typing import List
from Serializer.bus_serializer import bus_status_serializer


def route_serializer(data):
    return{
        "start_id":data.start_id,
        "end_id":data.end_id,
        "fare":data.fare,
        "distance":data.distance
    }

def area_serializer(data):
    return{
        "area_name":data.area_name
    }
def list_faculty_serializer(faculties) -> List:
    return [bus_status_serializer(faculty) for faculty in faculties]

def route_buses(data):
    return{
        "route_id":data.route_id,
        "bus_id":data.bus_id
    }