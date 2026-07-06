from sqlalchemy.orm import Session

from cyberinsight.models.scan import Scan
from sqlalchemy import func

class ScanRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, scan: Scan) -> Scan:
        self.db.add(scan)
        self.db.commit()
        self.db.refresh(scan)
        return scan

    def get_all(self):
        return (
            self.db.query(Scan)
            .order_by(Scan.created_at.desc())
            .all()
        )

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
    

    def count(self):
        return self.db.query(Scan).count()


    def average_score(self):
        return (
        self.db.query(func.avg(Scan.security_score))
        .scalar()
       )
   

    def highest_score(self):
       return (
        self.db.query(func.max(Scan.security_score))
        .scalar()
      )


    def lowest_score(self):
       return (
        self.db.query(func.min(Scan.security_score))
        .scalar()
      )


    def critical_scans(self):
       return (
        self.db.query(Scan)
        .filter(Scan.risk == "Critical")
        .count()
      )


    def recent(self, limit: int = 5):
       return (
        self.db.query(Scan)
        .order_by(Scan.created_at.desc())
        .limit(limit)
        .all()
    )