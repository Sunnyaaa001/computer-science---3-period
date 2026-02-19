from jose import jwt,JWTError


class TokenUtill:

    _secrect_key : str | None = None
    _algorithm: str = "HS256"

    @classmethod
    def init(cls,secret_key:str, algorithm: str = "HS256"):
        cls._secret_key = secret_key
        cls._algorithm = algorithm

    @classmethod
    def _check_init(cls):
        if not cls._secret_key:
            raise RuntimeError("TokenUtil not initialized")
    @classmethod    
    def create_token(cls,payload:dict)-> str:
        cls._check_init()
        return jwt.encode(claims=payload,key=cls._secret_key,algorithm=cls._algorithm)
    @classmethod
    def verify_token(cls,token:str)-> dict:
        cls._check_init()
        try:
            return jwt.decode(token=token,key=cls._secret_key,algorithms=cls._algorithm)
        except JWTError:
            return None