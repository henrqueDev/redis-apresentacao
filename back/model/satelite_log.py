import time
from timeit import timeit
from sqlalchemy import func
from sql_alchemy import banco
from datetime import datetime

class SateliteLogModel(banco.Model):
    __tablename__ = 'satelite_logs'

    satelite_log_id = banco.Column(banco.Integer, primary_key=True, autoincrement=True)
    data_hora = banco.Column(banco.DateTime, nullable=False)
    latitude = banco.Column(banco.Float, nullable=False)
    longitude = banco.Column(banco.Float, nullable=False)
    distancia_percorrida = banco.Column(banco.Float, nullable=False)

    def __init__(self, latitude, longitude, distancia_percorrida):
        self.data_hora = datetime.now()
        self.latitude = latitude
        self.longitude = longitude
        self.distancia_percorrida = distancia_percorrida


    @classmethod
    def get_last_register(cls):
        num = cls.query.filter(cls.satelite_log_id != None).count()
        previous_SateliteLog = cls.query.filter(cls.satelite_log_id == num).first()
        
        return previous_SateliteLog

    
    @classmethod
    def get_total_distance(cls):
        inicio = time.time()
        res = banco.session.query(func.sum(SateliteLogModel.distancia_percorrida).label('distancia_total')).first()
        metrics = time.time() - inicio
        return {'distancia_percorrida' : res[0], 'total_time' : metrics}

    def save(self):
        banco.session.add(self)
        banco.session.commit()