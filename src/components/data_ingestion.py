class DataIngestion:
    def __init__(self, source: str, dest: str):
        self.source = source
        self.dest = dest

    def ingest(self) -> tuple[str, str]:
        raise NotImplementedError

