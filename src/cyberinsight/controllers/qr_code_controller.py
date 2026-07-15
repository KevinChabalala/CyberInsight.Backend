# src/cyberinsight/controllers/qr_code_controller.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from cyberinsight.core.database import get_db
from cyberinsight.schemas.qr_code_schema import QRCodeCreate, QRCodeResponse, QRCodeUpdate
from cyberinsight.repositories.qr_code_repository import QRCodeRepository
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/", response_model=QRCodeResponse, status_code=status.HTTP_201_CREATED)
async def create_qr_code(
    qr_data: QRCodeCreate,
    db: Session = Depends(get_db)
):
    """Create a new QR code entry"""
    try:
        repo = QRCodeRepository(db)
        qr_code = repo.create(qr_data.model_dump())
        logger.info(f"QR code created with ID: {qr_code.id}")
        return qr_code
    except Exception as e:
        logger.error(f"Error creating QR code: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating QR code: {str(e)}"
        )

@router.get("/", response_model=List[QRCodeResponse])
async def get_all_qr_codes(
    user_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    """Get all QR codes, optionally filtered by user"""
    try:
        repo = QRCodeRepository(db)
        qr_codes = repo.get_all(user_id)
        return qr_codes
    except Exception as e:
        logger.error(f"Error fetching QR codes: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching QR codes: {str(e)}"
        )

@router.get("/{qr_code_id}", response_model=QRCodeResponse)
async def get_qr_code(
    qr_code_id: int,
    db: Session = Depends(get_db)
):
    """Get a specific QR code by ID"""
    repo = QRCodeRepository(db)
    qr_code = repo.get_by_id(qr_code_id)
    if not qr_code:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="QR code not found"
        )
    return qr_code

@router.put("/{qr_code_id}", response_model=QRCodeResponse)
async def update_qr_code(
    qr_code_id: int,
    update_data: QRCodeUpdate,
    db: Session = Depends(get_db)
):
    """Update a QR code"""
    repo = QRCodeRepository(db)
    qr_code = repo.update(qr_code_id, update_data.model_dump(exclude_unset=True))
    if not qr_code:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="QR code not found"
        )
    return qr_code

@router.delete("/{qr_code_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qr_code(
    qr_code_id: int,
    db: Session = Depends(get_db)
):
    """Delete a QR code"""
    repo = QRCodeRepository(db)
    deleted = repo.delete(qr_code_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="QR code not found"
        )
    return {"message": "QR code deleted successfully"}