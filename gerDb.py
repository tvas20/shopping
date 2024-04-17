from pydantic import BaseModel
import json

def getDB():
    with open('db.json', 'r') as dbj:
        db = json.load(dbj)
    return db

def saveDB(db):
    with open('db.json', 'w') as dbj:
        json.dump(db, fp=dbj, indent=4)

class Produto(BaseModel):
    codigo: str
    nome: str
    preco: float