from enum import Enum


class ErrorCode(Enum):
    """
    user error code
    """
    SERVER_ERROR = (500,"Server internal error")
    NO_PERMISSION = (403,"No permission!")
    RELOGIN = (401, "User information has expired. Please log in again.")
    ACCOUNT_EXIST = (500,"This account is already exists!")
    ACCOUNT_NOT_EXIST = (500,"This account is not exists!")
    INVALID_TOKEN = (401, "Invalid token!")
    INCORRECT_ACCOUNT_OR_PASSWORD = (500,"username or password is not correct!")
    """
    api category error code
    """
    NOT_UNIQUE_CATEGORY_NAME = (500,"This category name has already exist!")
    CATEGORY_NOT_FOUND = (500,"This category not found!")
    CATEGORY_PARENT_NOT_FOUND = (500,"parent doesn't exist!")
    SUB_CATEGORY_EXIST = (500,"This category has sub categories!")
    SUB_API_EXIST = (500,"This category has API!")
    CATEGORY_NAME_EXIST = (500, "This category name has already exist!")

    """
    api info error code
    """
    API_NAME_EXIST = (500,"This api name has already exists!")
    API_EXIST = (500,"This api has already exists!")
    API_MOT_EXIST = (500,"This API doesn't exist!")

    def __init__(self, code, msg):
        self.code = code
        self.msg = msg