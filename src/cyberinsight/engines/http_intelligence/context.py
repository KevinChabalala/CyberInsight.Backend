import requests


class HTTPScanContext:

    def __init__(
        self,
        response: requests.Response,
        response_time_ms: float,
    ):

        self.response = response

        self.response_time_ms = response_time_ms