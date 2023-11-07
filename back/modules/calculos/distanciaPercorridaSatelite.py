import math
import mpmath

def __toRad(latLong):
    latLong_rad = latLong * (3.141593 / 180)
    return latLong_rad

def __obterVariacaoLatLng(a,b):
    deltaA = a
    deltaB = b
    variacao = (deltaA - deltaB)
    if(variacao < 0):
        variacao = (deltaA - deltaB) * -1
    return __toRad(variacao)

def calcularDistanciaPercorrida(lat1,lat2,lng1,lng2):
    lx1 = (((math.sin(__obterVariacaoLatLng(lat1,lat2))/2)**2) + math.cos(__toRad(lat1))) * math.cos(__toRad(lat2)) * ((math.sin(__obterVariacaoLatLng(lng1,lng2)/2)) ** 2)
    try :
        lx3 = mpmath.atan(math.sqrt(lx1) / math.sqrt(1-lx1) )
        lx2 = 2 * lx3
    except ZeroDivisionError:
        lx2 = 0
    
    RaioTerra = 6371 # Km
    distanciaPercorrida = RaioTerra * lx2
    
    return float(distanciaPercorrida)