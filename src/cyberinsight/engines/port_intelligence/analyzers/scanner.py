import socket
from concurrent.futures import ThreadPoolExecutor


class PortScanner:

    TIMEOUT = 1

    @staticmethod
    def scan_port(host: str, port: int):

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
        )

        sock.settimeout(
            PortScanner.TIMEOUT
        )

        try:

            return (
                port,
                sock.connect_ex(
                    (host, port)
                )
                == 0,
            )

        finally:

            sock.close()

    @staticmethod
    def scan(host: str, ports: list[int]):

        results = {}

        with ThreadPoolExecutor(
            max_workers=50,
        ) as executor:

            futures = [

                executor.submit(
                    PortScanner.scan_port,
                    host,
                    port,
                )

                for port in ports
            ]

            for future in futures:

                port, is_open = future.result()

                results[port] = is_open

        return results