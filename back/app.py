from flask import Flask
from flask_restful import Api
from resources.satelite_log import SateliteLogResource

app = Flask(__name__)

api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5432/monit_iss'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api.add_resource(SateliteLogResource, '/iss')


if __name__ == '__main__':
    
    from sql_alchemy import banco
    banco.init_app(app)

    with app.app_context():
        try:
          banco.create_all()
        except Exception as exception:
          print("got the following exception when attempting db.create_all() in __init__.py: " + str(exception))
        finally:
          print("db.create_all() in __init__.py was successfull - no exceptions were raised")

    
    app.run(debug=True)

    
