from flask import Flask
from flask_restful import Api
from resources.satelite_log import SateliteLogResource
from client_redis import banco
app = Flask(__name__)

api = Api(app)

app.config['REDIS_URL'] = 'redis://localhost:6379'

api.add_resource(SateliteLogResource, '/iss')


if __name__ == '__main__':
    banco.init_app(app)
    app.run(debug=True)