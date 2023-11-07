import json
import requests
from calculos.distanciaPercorridaSatelite import calcularDistanciaPercorrida

def radarSateliteGet():
    try:
        
        res =  requests.get("https://api.wheretheiss.at/v1/satellites/25544")
        obj = json.loads(res.text)
        deslocamentoSatelite = calcularDistanciaPercorrida()
        return obj
    
    except requests.exceptions.JSONDecodeError as e:
        raise SystemExit(e)