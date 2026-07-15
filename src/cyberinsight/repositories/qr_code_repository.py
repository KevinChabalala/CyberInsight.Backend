# src/cyberinsight/repositories/qr_code_repository.py
from sqlalchemy.orm import Session
from typing import List, Optional
from cyberinsight.models.qr_code import QRCode

class QRCodeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, qr_code_data: dict) -> QRCode:
        qr_code = QRCode(**qr_code_data)
        self.db.add(qr_code)
        self.db.commit()
        self.db.refresh(qr_code)
        return qr_code

    def get_all(self, user_id: Optional[int] = None) -> List[QRCode]:
        query = self.db.query(QRCode)
        if user_id:
            query = query.filter(QRCode.user_id == user_id)
        return query.order_by(QRCode.created_at.desc()).all()

    def get_by_id(self, qr_code_id: int) -> Optional[QRCode]:
        return self.db.query(QRCode).filter(QRCode.id == qr_code_id).first()

    def update(self, qr_code_id: int, update_data: dict) -> Optional[QRCode]:
        qr_code = self.get_by_id(qr_code_id)
        if qr_code:
            for key, value in update_data.items():
                if value is not None:
                    setattr(qr_code, key, value)
            self.db.commit()
            self.db.refresh(qr_code)
        return qr_code

    def delete(self, qr_code_id: int) -> bool:
        qr_code = self.get_by_id(qr_code_id)
        if qr_code:
            self.db.delete(qr_code)
            self.db.commit()
            return True
        return False