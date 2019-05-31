import json
from random import choice
from random import randint
from time import sleep


def latitude():
    """
    Gera um valor para latitude.

    :return: (int) -90 <= val <= 90
    """
    y = randint(0, 90)
    return y * choice((-1, 1))  # longitude com hemisferio valido


def longitude():
    """
    Gera um valor para longitude.

    :return: (int) -180 <= val <= 180
    """
    x = randint(0, 180)
    return x * choice((-1, 1))  # longitude com hemisferio valido


def altitude(limiteInf=-20, limiteSup=100):
    """
    Gera um valor para altitude.

    :param limiteInf: (int) val < limiteSup
    :param limiteSup: (int) val > limiteInf
    :return: limiteInf <= val <= limiteSup
    """
    # altura usa limites porque não ha maximos e minimos bem definidos como em latitude e longitude
    return randint(limiteInf, limiteSup)


def getPosAtual(dict):
    """
    Posição atual do balão.

    :param dict: Dicionário com as informações de estado do balão.
    :return: [latitude, longitude, altura]
    """
    return [dict.get("latitude"), dict.get("longitude"), dict.get("altitude")]


def setPosAtual(dict, lat, long, alt):
    """
    Modifica a posição atual do balão.

    :param dict: Dicionário com as informações de estado do balão.
    :param lat: (int) nova latitude
    :param long: (int) nova longitude
    :param alt: (int) nova altura
    :return: indefinido
    """
    dict["latitude"] = lat
    dict["longitude"] = long
    dict["altitude"] = alt


def getPosicaoDesejada(dict):
    """
    Posição alvo para o balão.

    :param dict: Dicionário com as informações de localização para o balão.
    :return: [latitude, longitude, altura]
    """
    return [dict.get("alvoLatitude"), dict.get("alvoLongitude"), dict.get("alvoAltura")]


def setPosicaoDesejada(dict, lat, long, alt):
    """
    Modifica a posição alvo para o balão.

    :param dict: Dicionário com as informações de localização para o balão.
    :param lat: (int) nova latitude
    :param long: (int) nova longitude
    :param alt: (int) nova altura
    :return: indefinido
    """
    dict["alvoLatitude"] = lat
    dict["alvoLongitude"] = long
    dict["alvoAltura"] = alt


def getMaxDesvioAlvo(dict):
    """
        Desvio máximo aceitável do alvo para o balão.

        :param dict: Dicionário com as informações de localização para o balão.
        :return: [ desvio latitude, desvio longitude, desvio altura]
        """
    return [dict.get("desvioLatitude"), dict.get("desvioLongitude"), dict.get("desvioAltura")]


def setMaxDesvioAlvo(dict, lat, long, alt):
    """
    Modifica o desvio mácimo do alvo para o balão.

    :param dict: Dicionário com as informações de localização para o balão.
    :param lat: (int) nova latitude
    :param long: (int) nova longitude
    :param alt: (int) nova altura
    :return: indefinido
    """
    dict["desvioLatitude"] = lat
    dict["desvioLongitude"] = long
    dict["desvioAltura"] = alt


def setFlagMovimento(dict, val):
    """
    Modifica a flag que indica que o balão precisa se mover.

    :param dict: Dicionário com as informaçoes de estado do balão.
    :param val: (boolean)
    :return: indefinido
    """
    dict["movimento"] = val


def getFlagMovimento(dict):
    """
    Valor atual do status da movimentação do balao.

    :param dict: Dicionário com as informaçoes de estado do balão, adiciona a chave ao dicionario caso não exista.
    :return: (boolean)
    """
    return dict.setdefault("movimento", False)


def acionaMotores(dict):
    """
    Acionamento e lógica dos motores, forçosamente faz com que o balão passe pela origem da coordenada, o que não é bom
    no caso da logitude precisar ir de -179 para 179 e outras situções parecidas já que fará o balão tomar um caminho
    muito mais longo.
    Funciona com coordenadas com valores inteiros.

    :param dict: Dicionário com as informaçoes de estado do balão.
    :return: indefinido
    """
    posAtual = getPosAtual(dict)
    posDesejada = getPosicaoDesejada(dict)
    novaPos = posAtual
    if posAtual[0] != posDesejada[0]:  # latitudes sao diferentes
        if posDesejada[0] > posAtual[0]:  # força a passagem pela latitude zero (nao cruza os polos)
            novaPos[0] = posAtual[0] + 1
            dict["motorN"] = True
            dict["motorS"] = False
        else:
            novaPos[0] = posAtual[0] - 1
            dict["motorN"] = False
            dict["motorS"] = True
    if posAtual[1] != posDesejada[1]:  # longitude sao diferentes
        if posDesejada[1] > posAtual[1]:  # forca a passagem pela longitude zero e não pela menor distancia (problema)
            novaPos[1] = posAtual[1] + 1
            dict["motorL"] = True
            dict["motorO"] = False
        else:
            novaPos[1] = posAtual[1] - 1
            dict["motorL"] = False
            dict["motorO"] = True
    if posAtual[2] != posDesejada[2]:  # alturas sao diferentes
        if posDesejada[2] > posAtual[2]:  # forca a passagem pela altura zero
            novaPos[2] = posAtual[2] + 1
            dict["motorUp"] = True
            dict["motorDown"] = False
        else:
            novaPos[2] = posAtual[2] - 1
            dict["motorUp"] = False
            dict["motorDown"] = True
    setPosAtual(dict, *novaPos)


def desligaMotores(dict):
    """
    Desliga todos os motores do balão.

    :param dict: Dicionário com as informaçoes de estado do balão.
    :return: indefinido
    """
    dict["motorN"] = False
    dict["motorS"] = False
    dict["motorL"] = False
    dict["motorO"] = False
    dict["motorUp"] = False
    dict["motorDown"] = False


def emPosicao(dict):
    """
    Verifica se o balão chegou à posição alvo. Funciona para coordenadas com valores inteiros.

    :param dict: Dicionário com as informaçoes de estado do balão.
    :return: (boolean)
    """
    if getPosAtual(dict) == getPosicaoDesejada(dict):
        return True
    return False


def geraCoordenada():
    """
    Gera uma coordenada.

    :return: [latitude, longitude, altitude]
    """
    return [latitude(), longitude(), altitude()]


# ============================================================
with open("route.json", "r") as read_file:
    route = json.load(read_file)

# inicialização
getPosAtual(route)
setPosAtual(route, 0, 0, 0)
getPosicaoDesejada(route)
setPosicaoDesejada(route, 0, 0, 0)
setFlagMovimento(route, False)
desligaMotores(route)

while True:
    if emPosicao(route):
        setPosicaoDesejada(route, *geraCoordenada())
        setFlagMovimento(route, True)
    if getFlagMovimento(route):
        acionaMotores(route)
        if emPosicao(route):
            setFlagMovimento(route, False)
            desligaMotores(route)

    with open('route.json', 'w') as outfile:
        json.dump(route, outfile)

    print("Movimento: {mov}\n"
          "Posição atual: ({posA[0]}, {posA[1]}, {posA[2]})\n"
          "Posição desejada: ({posD[0]}, {posD[1]}, {posD[2]})\n\n".format(mov=getFlagMovimento(route),
                                                                           posA=getPosAtual(route),
                                                                           posD=getPosicaoDesejada(route)))
    sleep(1)
# ==================================================

#Estado Funcional
#{"sistema": true, "ip": "127.0.0.1", "mascara": "127.0.0.0", "porta": 4500, "status": 200, "dbs": 10, "conectado": "127.0.0.2", "latitude": 2, "longitude": 2, "maxLongitude": 2, "altitude": 1, "maxAltitude": 100,"movimento": false, "latP": 2, "longP": 2, "motorN": false, "motorS": false, "motorL": false, "motorO": false, "motorUp": true, "motorDown": false,"modo": "slave"}
