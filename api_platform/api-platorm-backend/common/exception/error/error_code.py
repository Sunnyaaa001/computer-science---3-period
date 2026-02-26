from enum import Enum


class ErrorCode(Enum):
    SERVER_ERROR = (500,"Server internal error")
    NO_PERMISSION = (403,"No permission!")
    RELOGIN = (401, "User information has expired. Please log in again.")
    ACCOUNT_EXIST = (500,"This account is already exists!")
    ACCOUNT_NOT_EXIST = (500,"This account is not exists!")
    INCORRECT_ACCOUNT_OR_PASSWORD = (500,"username or password is not correct!")
    
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg