from fastapi import FastAPI
from users.router import router

app = FastAPI()

app.include_router(router)


@app.get("/")
def hello():
    return {"message": "Hello, World! It's me, RTD!"}
