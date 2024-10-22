from http.client import HTTPException

from fastapi import APIRouter
from Models.user_models import UserResponse , UserLoginResponse
from Tables.user_tables import User
from Serializer.user_serializer import user_login_serializer , user_response_serializer
from Config.dependency import  db_dependency

user_router = APIRouter()


@user_router.get("/register")
async def user_register(response : UserResponse , db : db_dependency):
    db_user = User(**response.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return user_login_serializer(db_user)

@user_router.get("/login")
async def user_login(response : UserLoginResponse , db : db_dependency):
    db_user = db.query(User).filter(
        User.username == response.username ,
        User.password == response.password
    )
    if db_user is None :
        raise HTTPException(detail = "User Not Found " , status_code = 400)
    return user_login_serializer(db_user)