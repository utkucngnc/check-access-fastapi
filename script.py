from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from .util import GetConf

app = FastAPI()

# OAuth2 password bearer for authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User:
    def __init__(self, users: dict = GetConf().users,
                 token: str = Depends(oauth2_scheme)
                 ):
        self.token = token
        user = users.get(token)
        if user:
            self.role = user.role
            self.databases = user.databases
            self.ops = user.operations
        else:
            raise HTTPException(status_code=401, detail="Unauthorized")
        
    def get(self, db: str = None, col: str = None, id: int = 0):
        if db in self.databases or col in self.collections:
            return {'message': f'Get {db} {id}'}
        else:
            raise HTTPException(status_code=403, detail="Forbidden")
    
    def post(self, db: str = None, col: str = None, id: int = 0):
        if 'post' in self.ops.values():
            if db in self.databases or col in self.collections:
                return {'message': f'Post {db} {id}'}
            else:
                raise HTTPException(status_code=403, detail="Forbidden")
        else:
            raise HTTPException(status_code=403, detail="Forbidden")
    
    def put(self, db: str = None, col: str = None, id: int = 0):
        if 'put' in self.ops.values():
            if db in self.databases or col in self.collections:
                return {'message': f'Put {db} {id}'}
            else:
                raise HTTPException(status_code=403, detail="Forbidden")
        else:
            raise HTTPException(status_code=403, detail="Forbidden")
    
    def delete(self, db: str = None, col: str = None, id: int = 0):
        if 'delete' in self.ops.values():
            if db in self.databases or col in self.collections:
                return {'message': f'Delete {db} {id}'}
            else:
                raise HTTPException(status_code=403, detail="Forbidden")
        else:
            raise HTTPException(status_code=403, detail="Forbidden")