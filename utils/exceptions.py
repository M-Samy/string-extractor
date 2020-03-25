from utils import status_codes


class OperationResult(object):
    def __init__(self):
        self.status = False
        self.data = []
        self.message = ""
        self.status_code = status_codes.HTTP_400_BAD_REQUEST

    def __getstate__(self):
        return self.__dict__.copy()
