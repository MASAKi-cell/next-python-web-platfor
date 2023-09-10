class CustomError(Exception):
    def __init__(self, message="エラーが発生しました"):
        super().__init__(message)
