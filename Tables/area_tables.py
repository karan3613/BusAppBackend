from sqlalchemy import Boolean, Column, Integer, String, Float, ColumnElement
from Config.database import Base

# Table List
# Major Stops And Areas
# FAIR BTW AREAS DATABASE MERGE BUSES TRAVELLING BTW ROUTES
#  Route AND BUS


class Area(Base):
    __tablename__ = "areas"

    area_id = Column(Integer , primary_key=True , index= True , autoincrement=True)
    area_name = Column(String(50) , nullable = False)

class Route(Base):
    __tablename__ = "fairs"

    route_id = Column(Integer , primary_key= True , autoincrement = True)
    start_id = Column(Integer , index = True)
    end_id = Column(Integer , index = True)
    fare  = Column(Integer , nullable=False )
    distance = Column(Float , nullable=False)
class RouteBuses(Base):
    __tablename__ = "route_buses"

    route_id = Column(Integer, primary_key=True, index = True)
    bus_id = Column(Integer , nullable=False)