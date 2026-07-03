from datetime import datetime, timezone
from urllib.parse import urlparse

import whois

from .models import (
    DNSInfo,
    DomainScanResult,
    OwnerInfo,
    RegistrarInfo,
    RegistrationInfo,
)


class DomainEngine:

    @staticmethod
    def analyze(url: str) -> DomainScanResult:

        try:

            domain = urlparse(url).netloc or urlparse(url).path

            if domain.startswith("www."):
                domain = domain[4:]

            data = whois.whois(domain)

            # -------------------------
            # Handle date fields
            # -------------------------

            created = data.creation_date
            updated = data.updated_date
            expires = data.expiration_date

            if isinstance(created, list):
                created = created[0]

            if isinstance(updated, list):
                updated = updated[0]

            if isinstance(expires, list):
                expires = expires[0]

            now = datetime.now(timezone.utc)

            domain_age = None
            days_until_expiry = None
            expired = False

            if created:

                if created.tzinfo is None:
                    created = created.replace(
                        tzinfo=timezone.utc
                    )

                domain_age = (
                    now - created
                ).days // 365

            if expires:

                if expires.tzinfo is None:
                    expires = expires.replace(
                        tzinfo=timezone.utc
                    )

                days_until_expiry = (
                    expires - now
                ).days

                expired = days_until_expiry < 0

            # -------------------------
            # Name Servers
            # -------------------------

            name_servers = data.name_servers or []

            if not isinstance(name_servers, list):
                name_servers = [name_servers]

            name_servers = sorted(
                list(
                    set(name_servers)
                )
            )

            # -------------------------
            # DNSSEC Normalization
            # -------------------------

            dnssec_value = getattr(
                data,
                "dnssec",
                None,
            )

            dnssec_enabled = None

            if isinstance(dnssec_value, bool):

                dnssec_enabled = dnssec_value

            elif isinstance(dnssec_value, str):

                value = dnssec_value.strip().lower()

                if value == "signed":
                    dnssec_enabled = True

                elif value == "unsigned":
                    dnssec_enabled = False

            # -------------------------
            # Return Result
            # -------------------------

            return DomainScanResult(

                success=True,

                domain=domain,

                registrar=RegistrarInfo(
                    name=data.registrar,
                    url=getattr(
                        data,
                        "registrar_url",
                        None,
                    ),
                    abuse_email=getattr(
                        data,
                        "registrar_abuse_contact_email",
                        None,
                    ),
                    abuse_phone=getattr(
                        data,
                        "registrar_abuse_contact_phone",
                        None,
                    ),
                    iana_id=None,
                ),

                registration=RegistrationInfo(
                    created=created,
                    updated=updated,
                    expires=expires,
                    domain_age_years=domain_age,
                    days_until_expiry=days_until_expiry,
                    expired=expired,
                ),

                status=data.status or [],

                dns=DNSInfo(
                    dnssec=dnssec_enabled,
                    name_servers=name_servers,
                ),

                owner=OwnerInfo(
                    organization=getattr(
                        data,
                        "org",
                        None,
                    ),
                    country=getattr(
                        data,
                        "country",
                        None,
                    ),
                ),

                error=None,
            )



        except Exception as e:

            message = str(e).lower()

            # -------------------------
            # Friendly Error Messages
            # -------------------------

            if "no match for" in message:

                error_message = "Domain is not registered."

            elif "whois command returned no output" in message:

                error_message = "WHOIS information is unavailable for this domain."

            elif "connection timed out" in message:

                error_message = "WHOIS lookup timed out."

            elif "access denied" in message:

                error_message = "WHOIS server denied the request."

            else:

                error_message = "Unable to retrieve WHOIS information."

            return DomainScanResult(

                success=False,

                domain=domain if "domain" in locals() else "",

                registrar=RegistrarInfo(),

                registration=RegistrationInfo(),

                status=[],

                dns=DNSInfo(),

                owner=OwnerInfo(),

                error=error_message,
            )