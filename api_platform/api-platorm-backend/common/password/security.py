from passlib.context import CryptContext

class PasswordManager:
    
    _context = CryptContext(
        schemes=["argon2"],
        deprecated="auto"
    )

    @classmethod
    def hash(cls,text:str)->str:
        return cls._context.hash(text)
    
    @classmethod
    def vertify(cls,plain:str,hashed_text:str) ->bool:
        return cls._context.verify(plain,hashed_text)
               
