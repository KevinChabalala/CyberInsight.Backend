from cyberinsight.models.scan import Scan
from cyberinsight.repositories.scan_repository import ScanRepository
from cyberinsight.schemas.scan_schema import ScanCreate


class ScanService:

    def __init__(self, repository: ScanRepository):
        self.repository = repository

    def create_scan(self, request: ScanCreate, user_id):
        scan = Scan(
            user_id=user_id,
            url=str(request.url),
            status="PENDING",
            security_score=0,
        )

        return self.repository.create(scan)