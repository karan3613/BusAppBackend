from pydantic import BaseModel

class UserResponse(BaseModel):
    user_id: int
    first_name: str
    last_name: str | None = None  # Optional field
    age: int
    occupation: str
    email : str
    username : str
    password : str

class UserLoginResponse(BaseModel):
    username: str
    password: str