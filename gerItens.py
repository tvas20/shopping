import gerDb
import addGUI

def addItem(a,b,c):
    db = gerDb.getDB()
    try:
        novo = gerDb.Produto(codigo=a,nome=b,preco=c)
        db[novo.codigo] = novo.dict()
        gerDb.saveDB(db)
    except:
        return

def searchItem():
    db = gerDb.getDB()
    return db[input("codigo: ")]

def removeItem():
    db = gerDb.getDB()
    del db[input("codigo: ")]
    gerDb.saveDB(db)
"""
i = 27910
while i < 50000:
    try:
        i = addItem(i, 'nome', i)
        print(i)
    except:
        i = addItem(i, 'nome', i)
"""

