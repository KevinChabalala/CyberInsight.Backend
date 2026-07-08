from cyberinsight.engines.url import UrlEngine
from cyberinsight.engines.dns import DnsEngine
from cyberinsight.engines.ssl import SslEngine
from cyberinsight.engines.headers import HeaderEngine
from cyberinsight.engines.technology import TechnologyEngine
from cyberinsight.engines.scoring import ScoreEngine
from cyberinsight.engines.domain import DomainEngine
from cyberinsight.engines.dns_intelligence import DNSIntelligenceEngine
from cyberinsight.engines.http_intelligence import HTTPIntelligenceEngine
from cyberinsight.engines.port_intelligence import PortIntelligenceEngine
from cyberinsight.engines.tls_intelligence import TLSIntelligenceEngine

from cyberinsight.schemas.scan_report import ScanReport
from cyberinsight.schemas.dashboard_schema import DashboardResponse

from cyberinsight.models.scan import Scan
from cyberinsight.models.user import User

from cyberinsight.repositories.scan_repository import ScanRepository

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session


class ScanService:

    def __init__(self, db: Session):
        self.db = db

    def analyze(
        self,
        url: str,
        current_user: User,
    ):

        # -------------------------
        # Run Engines
        # -------------------------

        url_result = UrlEngine.analyze(url)

        dns_result = DnsEngine.analyze(url)

        ssl_result = SslEngine.analyze(url)

        header_result = HeaderEngine.analyze(url)

        technology_engine = TechnologyEngine()
        technology_result = technology_engine.analyze(url)

        domain_result = DomainEngine.analyze(url)

        dns_intelligence_result = DNSIntelligenceEngine.analyze(url)

        http_result = HTTPIntelligenceEngine.analyze(url)

        port_result = PortIntelligenceEngine.analyze(url)

        tls_result = TLSIntelligenceEngine.analyze(url)

        # -------------------------
        # Calculate Security Score
        # -------------------------

        score_engine = ScoreEngine()

        security_result = score_engine.calculate(
            url_result,
            dns_result,
            dns_intelligence_result,
            domain_result,
            ssl_result,
            header_result,
            http_result,
            technology_result,
            port_result,
            tls_result,
        )

        # -------------------------
        # Build Report
        # -------------------------

        report = ScanReport(
            url=url_result,
            dns=dns_result,
            dns_intelligence=dns_intelligence_result,
            ssl=ssl_result,
            headers=header_result,
            technology=technology_result,
            domain=domain_result,
            http_intelligence=http_result,
            port_intelligence=port_result,
            security=security_result,
            tls_intelligence=tls_result,
        )

        repository = ScanRepository(self.db)

        scan = Scan(
            user_id=current_user.id,
            url=url,
            status="COMPLETED",
            security_score=report.security.score,
            grade=report.security.rating,
            risk=report.security.risk,
            report=jsonable_encoder(report),
        )

        repository.create(scan)

        return report

    def get_history(
        self,
        current_user: User,
    ):

        repository = ScanRepository(self.db)

        return repository.get_all_by_user(current_user.id)

    def get_scan(
        self,
        scan_id,
        current_user: User,
    ):

        repository = ScanRepository(self.db)

        scan = repository.get_by_id(scan_id)

        if scan is None:
            raise HTTPException(
                status_code=404,
                detail="Scan not found",
            )

        if scan.user_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="Access denied",
            )

        return scan

    def get_dashboard(
        self,
        current_user: User,
    ):

        repository = ScanRepository(self.db)

        average = repository.average_score()

        return DashboardResponse(
            total_scans=repository.count(),
            average_score=int(average or 0),
            highest_score=repository.highest_score() or 0,
            lowest_score=repository.lowest_score() or 0,
            critical_scans=repository.critical_scans(),
            recent_scans=repository.recent(),
        )
