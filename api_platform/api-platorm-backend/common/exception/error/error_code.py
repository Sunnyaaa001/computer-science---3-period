from enum import Enum


class ErrorCode(Enum):
    SERVER_ERROR = (500,"Server internal error")
    NO_PERMISSION = (403,"No permission!")
    RELOGIN = (401, "User information has expired. Please log in again.")
    
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg