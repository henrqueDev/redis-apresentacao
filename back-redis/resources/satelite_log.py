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
        if banco.llen("sateliteLog:12") > 0:
            previous_SateliteLog = json.loads(banco.lrange("sateliteLog:12", -1, -1)[0])[0]

        if previous_SateliteLog is not None:
            r = banco.rpush("sateliteLog:12", json.dumps([{ "latitude": obj["latitude"], 
                                              "longitude": obj["longitude"], 
                                              "dist_percorrida": calcularDistanciaPercorrida(obj["latitude"], 
                                                previous_SateliteLog["latitude"], 
                                                obj["longitude"], previous_SateliteLog["longitude"])   
                                             }]))
        else:
            r = banco.rpush("sateliteLog:12", json.dumps([{ "latitude": obj["latitude"], 
                                              "longitude": obj["longitude"], 
                                              "dist_percorrida": 0 
                                             }]))
        if r:
            logs = banco.lrange("sateliteLog:12", 0, -1)

            
            total_distancia = 0.0

            for log_entry in logs:
                log_json = json.loads(log_entry)
                total_distancia += log_json[0]["dist_percorrida"]

            obj["distancia_percorrida_total"] = total_distancia

            
            return obj, 200
        else:
            return "Deu ruim", 200
