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
def getLongitude():
    with open("./data/dadosPosicionamento.json", "r") as read_file:
        dadosPosicionamento = json.load(read_file)
    return dadosPosicionamento["longitudeAtual"]
def getAltitude():
    with open("./data/dadosPosicionamento.json", "r") as read_file:
        dadosPosicionamento = json.load(read_file)
    return dadosPosicionamento["alturaAtual"]

def carregaJson(nome):
    """
    Tenta abrir o json para montar um dicionario a partir do mesmo.

    :param nome: nome do arquivo .json.
    :return: (dict) ou None
    """
    # faz no maximo n tentativas de leitura, para nao travar o sistema
    for i in range(30):
        try:
            # print("[jsonRead.carregaJson]", "tentativa de leitura num.", i+1, "em", nome)
            with open(nome) as arq:
                return json.load(arq)
        # nao pude acessar
        except PermissionError:
            # Esta em uso pelo sistema ou o arquivo realmente nao tem permissao de leitura
            pass
        # O arquivo nao existe ou "esta em uso pelo sistema"
        except FileNotFoundError as e:
            # quando um arquivo esta sendo salvo (sobrescrito) ele primeiramente e apagado e depois criado o novo
            # pode ocorrer de quando tentor acessar e arquivo estar sendo escrito por outra local
            pass
    return None
