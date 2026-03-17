from fastapi import FastAPI
from backend.api import router
from backend.deps import init_vectorstore

app = FastAPI()


@app.on_event("startup")
def startup_event():
    init_vectorstore()


app.include_router(router)