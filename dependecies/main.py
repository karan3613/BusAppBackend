from fastapi import FastAPI , HTTPException , status
from Config.database import engine
from Tables import bus_tables , area_tables , user_tables
from Routers.area_router import area_router
from Routers.bus_router import bus_router
from Routers.user_router import user_router
from mangum import Mangum
app = FastAPI()
handler = Mangum(app)

app.include_router(area_router , prefix= "/area")
app.include_router(bus_router , prefix = "/bus")
app.include_router(user_router , prefix="/user")

bus_tables.Base.metadata.create_all(bind=engine)
# area_tables.Base.metadata.create_all(bind=engine)
# user_tables.Base.metadata.create_all(bind=engine)



@app.get("/" , status_code= status.HTTP_201_CREATED)
async def home_page():
    return {"WELCOME TO THE HOME PAGE OF OUR API "}