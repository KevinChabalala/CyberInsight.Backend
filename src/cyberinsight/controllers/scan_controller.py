from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, status

from cyberinsight.core.database import get_db
from cyberinsight.core.dependencies import get_current_user
from cyberinsight.models.user import User
from cyberinsight.repositories.scan_repository import ScanRepository
from cyberinsight.schemas.scan_schema import ScanCreate, ScanResponse
from cyberinsight.services.scan_service import ScanService

router = APIRouter()


@router.post(
    "",
    response_model=ScanResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_scan(
    request: ScanCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    repository = ScanRepository(db)
    service = ScanService(repository)

    return service.create_scan(
        request,
        current_user.id,
    )