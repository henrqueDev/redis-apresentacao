import json
from flask import jsonify
from flask_restful import Resource, reqparse
import requests
from modules.calculos.distanciaPercorridaSatelite import calcularDistanciaPercorrida
from client_redis import banco

class SateliteLogResource(Resource):
    atributos = reqparse.RequestParser()

    def get(self):

        res =  requests.get("https://api.wheretheiss.at/v1/satellites/25544")
        obj = json.loads(res.text)
        
        previous_SateliteLog = None
        if previous_SateliteLog is not None:
            banco.hmset("SateliteLog", { "latitude": obj["latitude"], 
                                              "longitude": obj["longitude"], 
                                              "dist_percorrida": calcularDistanciaPercorrida(obj["latitude"], 
                                                previous_SateliteLog.latitude, 
                                                obj["longitude"], previous_SateliteLog.longitude)   
                                             })
        else:
            banco.hmset("SateliteLog", { "latitude": obj["latitude"], 
                                              "longitude": obj["longitude"], 
                                              "dist_percorrida": 0 
                                             })
            
        #obj["distancia_percorrida"] = SateliteLogModel.get_total_distance()
        return jsonify(obj)
