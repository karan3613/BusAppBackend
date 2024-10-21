
from sqlalchemy import Boolean , Column ,Integer , String , Float
from Config.database import Base

class User(Base):
    user_id = Column(Integer , primary_key= True , index= True)
    first_name = Column(String(50) , nullable=False)
    last_name = Column(String(50) , nullable= True )
    age = Column(Integer , nullable= False)
    occupation = Column(String(50) , nullable= False)

class UserLogin(Base):
    user_id = Column(Integer , primary_key= True  , index= True , autoincrement=True)
    username = Column(String(50))
    password = Column(String(50))