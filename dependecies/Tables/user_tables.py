
from sqlalchemy import Boolean , Column ,Integer , String , Float
from Config.database import Base

class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer , primary_key= True , index= True)
    first_name = Column(String(50) , nullable=False)
    last_name = Column(String(50) , nullable= True )
    age = Column(Integer , nullable= False)
    occupation = Column(String(50) , nullable= False)
    email = Column(String(50) , nullable = False  )
    username = Column(String(50) , nullable = False)
    password = Column(String(50) ,nullable = False )

