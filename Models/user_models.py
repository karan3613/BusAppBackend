from pydantic import BaseModel

class UserResponse(BaseModel):
    user_id: int
    first_name: str
    last_name: str | None = None  # Optional field
    age: int
    occupation: str

class UserLoginResponse(BaseModel):
    user_id: int
    username: str
    password: str