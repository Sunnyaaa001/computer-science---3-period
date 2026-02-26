from jose import jwt,JWTError


class TokenUtill:

    _secrect_key : str | None = None
    _algorithm: str = "HS256"
    _expire_time:int

    @classmethod
    def init(cls,secret_key:str, expire_time:int ,algorithm: str = "HS256",):
        cls._secret_key = secret_key
        cls._algorithm = algorithm
        cls._expire_time = expire_time

    @classmethod
    def _check_init(cls):
        if not cls._secret_key:
            raise RuntimeError("TokenUtil not initialized")
    @classmethod    
    def create_token(cls,payload:dict)-> str:
        cls._check_init()
        token=  jwt.encode(claims=payload,key=cls._secret_key,algorithm=cls._algorithm)
        return f"Bearer {token}"
    @classmethod
    def verify_token(cls,token:str)-> dict:
        cls._check_init()
        try:
            token = token.removeprefix("Bearer ").strip()
            return jwt.decode(token=token,key=cls._secret_key,algorithms=cls._algorithm)
        except JWTError:
            return None