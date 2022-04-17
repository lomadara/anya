from flask import Flask, Blueprint
from flask_restplus import Api
from werkzeug.contrib.fixers import ProxyFix
from flask_restplus.apidoc import apidoc
from flask_cors import CORS

from src.repository.db_connection import DbConnection

url_prefix = "/anya"
import os
class Server(object):
    def __init__(self):
        self.app = Flask(__name__, template_folder='{}\\templates'.format(os.path.dirname(os.path.abspath('src/templates'))))
        self.app.wsgi_app = ProxyFix(self.app.wsgi_app)
        apidoc.url_prefix = url_prefix
        self.blueprint = Blueprint('api', __name__, url_prefix=url_prefix)
        self.api = Api(
            doc='/docs',
            title="anya",
            description="anya api",
            version='0.0.1',
            contract='',
            default='anya',
            default_label='Anya'
        )
        
        self.api.init_app(self.blueprint)
        
        #self.health_check = self.health_check()
        
        self.app.register_blueprint(self.blueprint)
        
        CORS(self.app)
        
    # example of namespace creation    
    # def health_check(self):
    #     return self.api.namespace(
    #         name='Health Check',
    #         description='Endpoint to check if is application is alive',
    #         path='/health'
    #     )
    
    def run(self):
        self.app.run(
            debug=True,
            port=5000
        )

server = Server()

application = server.app

# @application.before_request
# def open_connection():
#     DbConnection().connect()
    
# @application.teardown_appcontext
# def close_connection():
#     DbConnection().disconnect()