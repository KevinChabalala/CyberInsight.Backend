import dns.resolver

from cyberinsight.engines.dns_intelligence.models import (
    DNSRecords,
    MXRecord,
    SOARecord,
)


class DNSRecordsAnalyzer:

    @staticmethod
    def get_records(domain: str) -> DNSRecords:

        records = DNSRecords()

        # -------------------------
        # A Records
        # -------------------------

        try:

            answers = dns.resolver.resolve(domain, "A")

            records.a = [
                answer.to_text()
                for answer in answers
            ]

        except Exception:
            pass

        # -------------------------
        # AAAA Records
        # -------------------------

        try:

            answers = dns.resolver.resolve(domain, "AAAA")

            records.aaaa = [
                answer.to_text()
                for answer in answers
            ]

        except Exception:
            pass

        # -------------------------
        # MX Records
        # -------------------------

        try:

            answers = dns.resolver.resolve(domain, "MX")

            records.mx = [

                MXRecord(
                    priority=answer.preference,
                    host=str(answer.exchange).rstrip("."),
                )

                for answer in answers

            ]

        except Exception:
            pass

        # -------------------------
        # NS Records
        # -------------------------

        try:

            answers = dns.resolver.resolve(domain, "NS")

            records.ns = [
                answer.to_text().rstrip(".").lower()
                for answer in answers
            ]

        except Exception:
            pass

        # -------------------------
        # TXT Records
        # -------------------------

        try:

            answers = dns.resolver.resolve(domain, "TXT")

            records.txt = [

                "".join(
                    part.decode()
                    for part in answer.strings
                )

                for answer in answers

            ]

        except Exception:
            pass

        # -------------------------
        # CNAME
        # -------------------------

        try:

            answers = dns.resolver.resolve(domain, "CNAME")

            records.cname = [
                answer.to_text().rstrip(".")
                for answer in answers
            ]

        except Exception:
            pass

        # -------------------------
        # SOA
        # -------------------------

        try:

            answer = dns.resolver.resolve(
                domain,
                "SOA",
            )[0]

            records.soa = SOARecord(

                primary_server=str(
                    answer.mname
                ).rstrip("."),

                admin_email=str(
                    answer.rname
                ).rstrip("."),

                serial=answer.serial,

            )

        except Exception:
            pass

        return records