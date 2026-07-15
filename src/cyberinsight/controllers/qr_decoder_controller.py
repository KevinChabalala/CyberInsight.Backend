# src/cyberinsight/controllers/qr_decoder_controller.py
from fastapi import APIRouter, File, UploadFile, HTTPException, Body, status
from typing import Dict, Any
import logging

from cyberinsight.services.qr_decoder_service import QRDecoderService

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/decode", status_code=status.HTTP_200_OK)
async def decode_qr_code(
    file: UploadFile = File(...)
) -> Dict[str, Any]:
    """
    Decode QR code from uploaded image file
    
    Args:
        file: Image file (PNG, JPG, JPEG, BMP, WEBP)
    
    Returns:
        Dict containing decoded data or error
    """
    try:
        # Log the request
        logger.info(f"Received QR decode request: {file.filename}")
        
        # Validate file type
        if not file.content_type or not file.content_type.startswith('image/'):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="File must be an image. Supported formats: PNG, JPG, JPEG, BMP, WEBP"
            )
        
        # Validate file size (10MB max)
        if file.size and file.size > 10 * 1024 * 1024:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="File size exceeds 10MB limit"
            )
        
        # Read file content
        contents = await file.read()
        
        if len(contents) == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Empty file uploaded"
            )
        
        logger.info(f"Processing file: {file.filename}, size: {len(contents)} bytes")
        
        # Decode QR code
        result = QRDecoderService.decode_from_bytes(contents)
        
        if result and result.get("success"):
            is_url = result.get("is_url", False)
            url = result.get("url")
            
            if is_url and url:
                logger.info(f"Successfully decoded QR code with URL: {url}")
                return {
                    "success": True,
                    "data": result["data"],
                    "url": url,
                    "is_url": True,
                    "message": result.get("message", "URL decoded successfully"),
                    "filename": file.filename
                }
            elif not is_url and url:
                # QR code contains text but not a valid URL
                logger.warning(f"QR code decoded but not a URL: {url}")
                return {
                    "success": True,
                    "data": result["data"],
                    "url": None,
                    "is_url": False,
                    "message": result.get("message", "QR code does not contain a valid URL"),
                    "filename": file.filename,
                    "content": result["data"]
                }
            else:
                # QR code decoded but no URL found
                return {
                    "success": True,
                    "data": result["data"],
                    "url": None,
                    "is_url": False,
                    "message": "QR code does not contain a valid URL",
                    "filename": file.filename,
                    "content": result["data"]
                }
        else:
            error_msg = result.get("error", "Failed to decode QR code")
            logger.warning(f"Failed to decode QR code from {file.filename}: {error_msg}")
            return {
                "success": False,
                "error": error_msg,
                "filename": file.filename,
                "message": "No QR code found in the image"
            }
            
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Unexpected error in QR decode: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing image: {str(e)}"
        )

@router.post("/decode-base64")
async def decode_qr_code_base64(
    data: Dict[str, str] = Body(...)
) -> Dict[str, Any]:
    """
    Decode QR code from base64 encoded image
    
    Args:
        data: JSON with 'image' field containing base64 data
    
    Returns:
        Dict containing decoded data or error
    """
    try:
        if 'image' not in data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No image data provided"
            )
        
        logger.info("Received base64 QR decode request")
        
        result = QRDecoderService.decode_from_base64(data['image'])
        
        if result and result.get("success"):
            is_url = result.get("is_url", False)
            url = result.get("url")
            
            if is_url and url:
                logger.info("Successfully decoded QR code with URL from base64")
                return {
                    "success": True,
                    "data": result["data"],
                    "url": url,
                    "is_url": True,
                    "message": result.get("message", "URL decoded successfully")
                }
            else:
                return {
                    "success": True,
                    "data": result["data"],
                    "url": None,
                    "is_url": False,
                    "message": result.get("message", "QR code does not contain a valid URL"),
                    "content": result["data"]
                }
        else:
            error_msg = result.get("error", "Failed to decode QR code")
            logger.warning(f"Failed to decode QR code from base64: {error_msg}")
            return {
                "success": False,
                "error": error_msg,
                "message": "No QR code found in the image"
            }
            
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Unexpected error in QR decode: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing image: {str(e)}"
        )

@router.get("/health")
async def health_check() -> Dict[str, Any]:
    """Health check endpoint for QR decoder"""
    return {
        "status": "healthy",
        "service": "qr-decoder",
        "version": "1.0.0",
        "endpoints": {
            "/qr/decode": "POST - Upload image to decode QR code",
            "/qr/decode-base64": "POST - Decode QR code from base64 data",
            "/qr/health": "GET - Health check"
        }
    }