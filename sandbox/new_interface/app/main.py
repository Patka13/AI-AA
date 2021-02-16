'''from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return{"title": "Hello AI"}
'''
from fastapi import FastAPI
from pydantic import BaseModel
#import requestscd
app = FastAPI()

db=[]

class User(BaseModel):
    imie: str
    nazwisko: str
    email: str
    bank : str
    wydatek: str
    kwota: int

@app.get('/')
def index():
    return {'key' : 'value'}
    
@app.get('/users')
def get_users():
    
    return db

@app.get('/users/{user_id}')
def get_user(user_id: int):
    return db[user_id-1]
@app.post('/users')
def create_user(user: User):
    db.append(user.dict())
    return db[-1]
@app.delete('/user/{user_id}')
def delete_user(user_id: int):
    db.pop(user_id-1)
    return{}
