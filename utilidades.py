import json
import functools


def calcular_frecuencia(texto):
    tiempos = (365*24*3600,30*24*3600,7*24*3600,24*3600,3600,60,1)
    partes = map(lambda x: int(x[:-1]), texto.split(":"))
    total_seg = functools.reduce(lambda acc,x: acc+x[0]*x[1],zip(tiempos,partes),0)
    return total_seg


def leer_jobs(path):
    trabajos = []
    with open(path, "r") as f:
        trabajos = json.loads(f.read())

    for i,j in enumerate(trabajos):
        j["id"] = i
        j["frecuencia"] = calcular_frecuencia(j["frecuencia"]) 
        j["ultima_ejecucion"] = 0

    return trabajos