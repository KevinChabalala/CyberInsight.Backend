# src/cyberinsight/controllers/__init__.py
from .auth_controller import router as auth_router
from .scan_controller import router as scan_router
from .qr_decoder_controller import router as qr_router

__all__ = ["auth_router", "scan_router", "qr_router"]