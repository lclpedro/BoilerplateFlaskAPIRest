from tinymongo import TinyMongoClient

'''
Criação da função construtora e definição de quem irá utilizar a database.
'''

def get_db():
    conect = TinyMongoClient()
    db = conect.contact
    return db

def configure(app):
    app.db = get_db()