from fastapi import FastAPI
from src.api.upload import router
app = FastAPI()


@app.get("/")
def home():
    return {"message": "Backend Running"}

app.include_router(router)