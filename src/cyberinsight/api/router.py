from fastapi import APIRouter

from cyberinsight.controllers.auth_controller import router as auth_router
from cyberinsight.controllers.scan_controller import router as scan_router
from cyberinsight.controllers.qr_decoder_controller import router as qr_router

api_router = APIRouter()

api_router.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"],
)

api_router.include_router(
    scan_router,
    prefix="/scans",
    tags=["Scans"],
)

api_router.include_router(
    qr_router,
    prefix="/qr",
    tags=["QR Decoder"],
)