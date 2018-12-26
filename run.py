import os

from flask import Flask

import views

'''
Criando a fábrica de inicialização da applicação.
'''

def create_app(test_config=None):
    
    '''
    Flask(__name__, instance_relative_config=True )
    instance_relative_config=True informa ao aplicativo que os arquivos de configuração são 
    relativos à pasta da instância. A pasta da instância está localizada fora do flaskr pacote 
    e pode conter dados locais que não devem ser confirmados no controle de versão, como 
    segredos de configuração e o arquivo de banco de dados.
    '''

    app=Flask(__name__)

    if not test_config is None:
        #Carrega da configuração de teste se ela for passada.
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except Exception as error:
        print(str(error))
    
    views.configure(app)
    
    return app
