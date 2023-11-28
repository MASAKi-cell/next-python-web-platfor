from enum import Enum


class HttpCode(Enum):
    OK = 200
    NO_CONTENT = 204
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    UNPROCESSABLE_CONTENT = 422
    INTERNAL_SERVER_ERROR = 500


class ExceptionsError(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return "f{self.status_code}: {self.message}"
