from jose import jwt,JWTError


class TokenUtill:

    def __init__(self,secret_key:str, algorithm: str = "HS256"):
        self.secret_key = secret_key
        self.algorithm = algorithm

    def create_token(self,payload:dict)-> str:
        return jwt.encode(claims=payload,key=self.secret_key,algorithm=self.algorithm)
    
    def verify_token(self,token:str)-> dict:
        try:
            return jwt.decode(token=token,key=self.secret_key,algorithms=self.algorithm)
        except JWTError:
            return None