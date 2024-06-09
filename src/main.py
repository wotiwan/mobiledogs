from fastapi import FastAPI
from users.router import router
from devices.router import device_router

app = FastAPI()

app.include_router(router, prefix="/users")
app.include_router(device_router, prefix="/devices")


@app.get("/")
def hello():
    return {"message": "Hello, World! It's me, RTD!"}
