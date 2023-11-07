import json
from flask import jsonify
from flask_restful import Resource, reqparse
import requests
from model.satelite_log import SateliteLogModel
from modules.calculos.distanciaPercorridaSatelite import calcularDistanciaPercorrida
import cProfile

class SateliteLogResource(Resource):
    atributos = reqparse.RequestParser()

    def get(self):
        res =  requests.get("https://api.wheretheiss.at/v1/satellites/25544")
        obj = json.loads(res.text)
        
        previous_SateliteLog = SateliteLogModel.get_last_register()
        if previous_SateliteLog is not None:
            log = SateliteLogModel(obj["latitude"], obj["longitude"], calcularDistanciaPercorrida(obj["latitude"], 
                            previous_SateliteLog.latitude, 
                            obj["longitude"], previous_SateliteLog.longitude))
            log.save()
        else:
            log = SateliteLogModel(obj["latitude"], obj["longitude"], 0)
            log.save()
        obj["distancia_percorrida_total"] = SateliteLogModel.get_total_distance()
        return jsonify(obj)
