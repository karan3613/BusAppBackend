from collections import Counter

from sqlalchemy import Boolean , Column ,Integer , String , Float
from Config.database import Base

# Table List
# Bus
# Bus_Location
# Bus_Status
# Bus_RouteDataBase

class Bus(Base):
    __tablename__ = "buses"

    bus_id = Column(Integer , primary_key=True , index = True , autoincrement=True)
    bus_no = Column(String(50) , unique = True)
    driver_name = Column(String(50))
    conducter_name = Column(String(50))
    conducter_contact = Column(String(50))

class BusLocation(Base):
    __tablename__ = "buses_location"

    bus_id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float , nullable= False)
    longitude = Column(Float , nullable= False)
    shard_id = Column(Integer)

class BusStatus(Base):
    __tabelname__ = "buses_status"

    bus_id = Column(Integer, primary_key=True, index=True)
    status = Column(Boolean , nullable= False)
    bus_no = Column(String(50) , unique = True)

class BusRoute(Base):
    __tablename__ = "buses_routes"

    bus_id = Column(Integer, primary_key=True, index=True)
    stop1 = Column(Integer , nullable=True)
    stop2 = Column(Integer, nullable=True)
    stop3 = Column(Integer, nullable=True)
    stop4 = Column(Integer, nullable=True)
    stop5 = Column(Integer, nullable=True)