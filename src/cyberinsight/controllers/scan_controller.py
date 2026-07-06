from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from cyberinsight.core.database import get_db
from cyberinsight.schemas.scan_schema import ScanRequest
from cyberinsight.services.scan_service import ScanService

router = APIRouter()


@router.post("/")
def scan(
    request: ScanRequest,
    db: Session = Depends(get_db),
):
    service = ScanService(db)

    return service.analyze(
        str(request.url)
    )