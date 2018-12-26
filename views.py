from flask import jsonify
def configure(app):
    @app.route('/')
    def init_app():
        return jsonify(code=200, data='Aplicação inicializada com sucesso. Pode começar a desenvolver os seus módulos.'), 200 

