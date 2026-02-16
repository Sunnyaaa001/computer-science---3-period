from common.exception.error.error_code import ErrorCode

class BusinessException(Exception):

    def __init__(self,err:ErrorCode):
        self.code = err.code
        self.message = self.message
            