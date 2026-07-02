from sqlalchemy.orm import Session

from cyberinsight.models.scan import Scan


class ScanRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, scan: Scan) -> Scan:
        self.db.add(scan)
        self.db.commit()
        self.db.refresh(scan)
        return scan

    def get_all_by_user(self, user_id):
        return (
            self.db.query(Scan)
            .filter(Scan.user_id == user_id)
            .all()
        )

    def get_by_id(self, scan_id):
        return (
            self.db.query(Scan)
            .filter(Scan.id == scan_id)
            .first()
        )