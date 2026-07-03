class TLSContext:

    def __init__(
        self,
        hostname,
        connection,
        certificate,
    ):
        self.hostname = hostname
        self.connection = connection
        self.certificate = certificate