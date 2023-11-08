from flask import Flask
from flask_restful import Api
from resources.satelite_log import SateliteLogResource
from client_redis import banco
from flask_cors import CORS
app = Flask(__name__)

CORS(app)

api = Api(app)

api.add_resource(SateliteLogResource, '/iss')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)