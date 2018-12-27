import os
import database
import admin

from flask import Flask, jsonify
from flask_cors import CORS


'''
Criando a fábrica de inicialização da applicação.
'''

def create_app():
    
    '''
    Flask(__name__, instance_relative_config=True )
    instance_relative_config=True informa ao aplicativo que os arquivos de configuração são 
    relativos à pasta da instância. A pasta da instância está localizada fora do flaskr pacote 
    e pode conter dados locais que não devem ser confirmados no controle de versão, como 
    segredos de configuração e o arquivo de banco de dados.
    '''

    app=Flask(__name__) 

    '''
    DECLARAÇÃO DE EXTENSÕES DA APLICAÇÃO
    '''

    database.configure(app)
    admin.configure(app)
    
    '''
    DECLARAÇÃO DE VARIAVEIS DA APLICAÇÃO
    '''

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


    @app.route('/', methods=['GET'])
    def init_app():
        return jsonify(code=200, data='Aplicação inicializada com sucesso. Pode começar a desenvolver os seus módulos. http://localhost:5000/admin/contactview/'), 200
    
    return app
