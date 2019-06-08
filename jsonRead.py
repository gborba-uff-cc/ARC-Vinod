
def getIp():
    with open("infosRoteador.json", "r") as read_file:
        infosRoteador.json = json.load(read_file)
    return infosRoteador.json["ip"]

def getMasterIp():
    with open("infosRoteador.json", "r") as read_file:
        infosRoteador.json = json.load(read_file)
    return infosRoteador.json["conectado"]

def getType():
    with open("infosRoteador.json", "r") as read_file:
        infosRoteador.json = json.load(read_file)
    return infosRoteador.json["modo"]

def getLatitude():
    with open("dadosPosicionamento.json", "r") as read_file:
        dadosPosicionamento.json = json.load(read_file)
    return dadosPosicionamento.json["latitudeAtual"]

