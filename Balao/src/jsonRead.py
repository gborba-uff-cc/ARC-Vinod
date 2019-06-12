import json

def getIp():
    with open("./data/infosRoteador.json", "r") as read_file:
        infosRoteador = json.load(read_file)
    return infosRoteador["ip"]

def getMasterIp():
    with open("./data/infosRoteador.json", "r") as read_file:
        infosRoteador = json.load(read_file)
    return infosRoteador["conectado"]

def getType():
    with open("./data/infosRoteador.json", "r") as read_file:
        infosRoteador = json.load(read_file)
    return infosRoteador["modo"]

def getLatitude():
    with open("./data/dadosPosicionamento.json", "r") as read_file:
        dadosPosicionamento = json.load(read_file)
    return dadosPosicionamento["latitudeAtual"]