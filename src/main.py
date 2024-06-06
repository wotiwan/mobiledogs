from fastapi import FastAPI
from users.router import router
from devices.router import device_router

app = FastAPI()

app.include_router(router)
app.include_router(device_router)


@app.get("/")
def hello():
    return {"message": "Hello, World! It's me, RTD!"}
