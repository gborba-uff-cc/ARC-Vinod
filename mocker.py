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


def getPosAtual(dictPos):
    """
    Posição atual do balão.

    :param dictPos: Dicionário com as informações de estado do balão.
    :return: [latitude, longitude, altura]
    """
    return [dictPos["latitudeAtual"], dictPos["longitudeAtual"], dictPos["alturaAtual"]]


def setPosAtual(dictPos, lat, long, alt):
    """
    Modifica a posição atual do balão.

    :param dictPos: Dicionário com as informações de estado do balão.
    :param lat: (int) nova latitude
    :param long: (int) nova longitude
    :param alt: (int) nova altura
    :return: indefinido
    """
    dictPos["latitudeAtual"] = lat
    dictPos["longitudeAtual"] = long
    dictPos["alturaAtual"] = alt


def getPosicaoDesejada(dictServer):
    """
    Posição alvo para o balão.

    :param dictServer: Dicionário com as infromações de posicionamento enviadas pelo servidor.
    :return: [latitude, longitude, altura]
    """
    return [dictServer["alvoLatitude"], dictServer["alvoLongitude"], dictServer["alvoAltura"]]


def setPosicaoDesejada(dictServer, lat, long, alt):
    """
    Modifica a posição alvo para o balão.

    :param dictServer: Dicionário com as infromações de posicionamento enviadas pelo servidor.
    :param lat: (int) nova latitude
    :param long: (int) nova longitude
    :param alt: (int) nova altura
    :return: indefinido
    """
    dictServer["alvoLatitude"] = lat
    dictServer["alvoLongitude"] = long
    dictServer["alvoAltura"] = alt


def getMaxDesvioAlvo(dictServer):
    """
    Desvio máximo aceitável do alvo para o balão.

    :param dictServer: Dicionário com as infromações de posicionamento enviadas pelo servidor.
    :return: [ desvio latitude, desvio longitude, desvio altura]
    """
    return [dictServer["desvioLatitude"], dictServer["desvioLongitude"], dictServer["desvioAltura"]]


def setMaxDesvioAlvo(dictServer, lat, long, alt):
    """
    Modifica o desvio mácimo do alvo para o balão.

    :param dictServer: Dicionário com as infromações de posicionamento enviadas pelo servidor.
    :param lat: (int) nova latitude
    :param long: (int) nova longitude
    :param alt: (int) nova altura
    :return: indefinido
    """
    dictServer["desvioLatitude"] = lat
    dictServer["desvioLongitude"] = long
    dictServer["desvioAltura"] = alt


def setFlagMovimento(dictPos, val):
    """
    Modifica a flag que indica que o balão precisa se mover.

    :param dictPos: Dicionário com as informações de estado do balão.
    :param val: (boolean)
    :return: indefinido
    """
    dictPos["movimentando"] = val


def getFlagMovimento(dictPos):
    """
    Valor atual do status da movimentação do balao.

    :param dictPos: Dicionário com as informações de estado do balão.
    :return: (boolean)
    """
    return dictPos["movimentando"]


def acionaMotores(dictPos, dictServer):
    """
    Acionamento e lógica dos motores, forçosamente faz com que o balão passe pela origem da coordenada, o que não é bom
    no caso da logitude precisar ir de -179 para 179 e outras situções parecidas já que fará o balão tomar um caminho
    muito mais longo.
    Funciona com coordenadas com valores inteiros.

    :param dictPos: Dicionário com as informações de estado do balão.
    :param dictServer: Dicionário com as infromações de posicionamento enviadas pelo servidor.
    :return: indefinido
    """
    posAtual = getPosAtual(dictPos)
    posDesejada = getPosicaoDesejada(dictServer)
    novaPos = posAtual
    if posAtual[0] != posDesejada[0]:  # latitudes sao diferentes
        if posDesejada[0] > posAtual[0]:  # força a passagem pela latitude zero (nao cruza os polos)
            novaPos[0] = posAtual[0] + 1
            dictPos["motorN"] = True
            dictPos["motorS"] = False
        else:
            novaPos[0] = posAtual[0] - 1
            dictPos["motorN"] = False
            dictPos["motorS"] = True
    if posAtual[1] != posDesejada[1]:  # longitude sao diferentes
        if posDesejada[1] > posAtual[1]:  # forca a passagem pela longitude zero e não pela menor distancia (problema)
            novaPos[1] = posAtual[1] + 1
            dictPos["motorL"] = True
            dictPos["motorO"] = False
        else:
            novaPos[1] = posAtual[1] - 1
            dictPos["motorL"] = False
            dictPos["motorO"] = True
    if posAtual[2] != posDesejada[2]:  # alturas sao diferentes
        if posDesejada[2] > posAtual[2]:  # forca a passagem pela altura zero
            novaPos[2] = posAtual[2] + 1
            dictPos["motorUp"] = True
            dictPos["motorDown"] = False
        else:
            novaPos[2] = posAtual[2] - 1
            dictPos["motorUp"] = False
            dictPos["motorDown"] = True
    setPosAtual(dictPos, *novaPos)


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


def emPosicao(dictDados, dictServer):
    """
    Verifica se o balão chegou à posição alvo observando a precisão exigida pelo servidor.
    Funciona para coordenadas com valores inteiros.

    :param dictDados: Dicionário com as informaçoes de estado do balão.
    :param dictServer: Dicionário com as infromações de posicionamento enviadas pelo servidor.
    :return: (boolean)
    """
    posAlvo = getPosicaoDesejada(dictServer)
    desvio = getMaxDesvioAlvo(dictServer)
    limInferior = [posAlvo[0] - desvio[0], posAlvo[1] - desvio[1], posAlvo[2] - desvio[2]]
    limSuperior = [posAlvo[0] + desvio[0], posAlvo[1] + desvio[1], posAlvo[2] + desvio[2]]
    if limInferior <= getPosAtual(dictDados) <= limSuperior:
        return True
    return False


def geraCoordenada():
    """
    Gera uma coordenada.

    :return: [latitude, longitude, altitude]
    """
    return [latitude(), longitude(), altitude()]


def modificacaoDadosPermitida(dictFlags):
    """
    Retorna a permissão para a escrita da posição atual.

    :param dictFlags: Dicionário com as flags que o servidor envia para o balão.
    :return: (boolean)
    """
    return not dictFlags["lendoDadosPosicionamento"]


def carregaJson(nome):
    """
    Tenta abrir o json, até conseguir, para montar um dicionário a partir do mesmo.

    :param nome: nome do arquivo .json.
    :return: (dict)
    """
    while True:
        try:
            with open(nome) as arq:
                return json.load(arq)
        # não pude acessar
        except PermissionError:
            # Está em uso pelo sistema ou o arquivo realmente não tem permissão de leitura
            pass
        # quando um arquivo esta sendo salvo (sobrescrito) ele primeiramente é apagado e depois criado o novo
        # pode ocorrer de quando tentor acessar e arquivo estar sendo escrito por outra local
        except FileNotFoundError as e:
            # O arquivo não existe ou "está em uso pelo sistema"
            pass

def gravaJson(dict, nome):
    """
    Monta um dicionário a partir de um arquivo .json.

    :param dict: Dicionário com o que será escrito
    :param nome: Nome do arquivo .json que será escrito.
    :return: (dict)
    """
    with open(nome, 'w') as arq:
        json.dump(dict, arq)


def sistemaAtivo(dictFlags):
    """
    Lê a flag de controle remoto; se o servidor ligou este balão ou não.

    :param dictFlags: Dicionário com as flags que o servidor envia para o balão.
    :return: (boolean)
    """
    return dictFlags["sistema"]

# ============================================================
# REVISAR COM CALMA
NOME_ARQ_POSICIONAMENTO_SERVER = "posicionamentoServer.json"
NOME_ARQ_DADOS_POSICIONAMENTO = "dadosPosicionamento.json"
# sem uso
# NOME_ARQ_INFOS_REDE = "infosRoteador.json"
NOME_ARQ_FLAGS_SERVER = "flagsServer.json"
# inicialização
dadosPos = carregaJson(NOME_ARQ_DADOS_POSICIONAMENTO)
setFlagMovimento(dadosPos, False)
desligaMotores(dadosPos)
while True:
    flags = carregaJson(NOME_ARQ_FLAGS_SERVER)
    if sistemaAtivo(flags):
        posAlvo = carregaJson(NOME_ARQ_POSICIONAMENTO_SERVER)
        # rede = carregaJson(NOME_ARQ_INFOS_REDE)
        # #  [PARA TESTE]
        # if emPosicao(dadosPos, posAlvo):
        #     setPosicaoDesejada(posAlvo, *geraCoordenada())
        #     gravaJson(posAlvo, NOME_ARQ_POSICIONAMENTO_SERVER)
        # # fim [PARA TESTE]
        if not emPosicao(dadosPos, posAlvo):
            setFlagMovimento(dadosPos, True)
        if getFlagMovimento(dadosPos):
            acionaMotores(dadosPos, posAlvo)
            if emPosicao(dadosPos, posAlvo):
                setFlagMovimento(dadosPos, False)
                desligaMotores(dadosPos)
        if modificacaoDadosPermitida(flags):
            gravaJson(dadosPos, NOME_ARQ_DADOS_POSICIONAMENTO)
        print("========================================\n"
              "Flag Sistema    : {f}\n"
              "-----------------\n"
              "Movimento       : {mov}\n"
              "Posição atual   : ({posA[0]}, {posA[1]}, {posA[2]})\n"
              "Posição desejada: ({posD[0]}, {posD[1]}, {posD[2]})\n"
              "Desvio permitido: ({desP[0]}, {desP[1]}, {desP[2]})\n"
              "========================================\n".format(f=sistemaAtivo(flags),
                                                                  mov=getFlagMovimento(dadosPos),
                                                                  posA=getPosAtual(dadosPos),
                                                                  posD=getPosicaoDesejada(posAlvo),
                                                                  desP=getMaxDesvioAlvo(posAlvo)))
    else:
        print("========================================\n"
              "Flag Sistema    : {}\n"
              "-----------------\n"
              "    Sistema em stand-by\n"
              "========================================\n".format(sistemaAtivo(flags)))
    sleep(1)
# ==================================================

# Estado funcional dos .json's
# =>flagsServer
# {"sistema": true, "lendoDadosPosicionamento": false, "modificandoPosicionamentoAlvo": false,
# "modificandoInfosRoteador": false}
# =>posicionamentoServer
# {"alvoLatitude": 0, "alvoLongitude": 0, "alvoAltura": 0, "desvioLatitude": 0, "desvioLongitude": 0, "desvioAltura": 0}
# =>dadosPosicionamento
# {"latitudeAtual": 0, "longitudeAtual": 0, "alturaAtual": 30, "movimentando": true, "motorN": false, "motorS": false,
# "motorL": false, "motorO": false, "motorUp": false, "motorDown": true, "altitudeAtual": 29}
# =>infosRoteador
# {"sistema": true, "conectado": "127.0.0.2", "ip": "127.0.0.1", "mascara": "127.0.0.0", "modo": "slave", "porta": 4500,
# "status": 200, "dbs": 10}
