from uuid import UUID
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from cyberinsight.core.database import get_db
from cyberinsight.core.dependencies import get_current_user

from cyberinsight.models.user import User

from cyberinsight.schemas.scan_schema import ScanRequest
from cyberinsight.schemas.scan_history_schema import ScanHistoryItem
from cyberinsight.schemas.scan_detail_schema import ScanDetailResponse
from cyberinsight.schemas.dashboard_schema import DashboardResponse

from cyberinsight.services.scan_service import ScanService

router = APIRouter()


@router.post("/")
def scan(
    request: ScanRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = ScanService(db)

    return service.analyze(
        str(request.url),
        current_user,
    )


@router.get(
    "/",
    response_model=List[ScanHistoryItem],
)
def get_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = ScanService(db)

    return service.get_history(
        current_user,
    )


@router.get(
    "/dashboard",
    response_model=DashboardResponse,
)
def dashboard(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = ScanService(db)

    return service.get_dashboard(
        current_user,
    )


@router.get(
    "/{scan_id}",
    response_model=ScanDetailResponse,
)
def get_scan(
    scan_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = ScanService(db)

    return service.get_scan(
        scan_id,
        current_user,
    )