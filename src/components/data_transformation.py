class DataTransformation:
    def __init__(self, input_train: str, input_test: str):
        self.input_train = input_train
        self.input_test = input_test

    def transform(self) -> tuple[str, str]:
        raise NotImplementedError

