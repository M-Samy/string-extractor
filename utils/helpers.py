from utils import status_codes
from utils.exceptions import OperationResult


def validate(string_list=None):
    result = OperationResult()
    try:
        if isinstance(string_list, list) and len(string_list):
            result.status = True
            result.status_code = status_codes.HTTP_200_OK
        return result
    except Exception as err:
        raise err
