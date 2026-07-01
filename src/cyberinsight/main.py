from contextlib import asynccontextmanager

from fastapi import FastAPI

from cyberinsight.api.router import api_router
from cyberinsight.config.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(" CyberInsight Backend Starting...")
    yield
    print(" CyberInsight Backend Stopped.")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
    lifespan=lifespan,
)

app.include_router(api_router)


@app.get("/", tags=["Home"])
async def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
        "message": "Welcome to CyberInsight Backend"
    }