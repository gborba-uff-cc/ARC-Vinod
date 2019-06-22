import json
# import os  # TESTE


def gravaJson(dict, nome):
    """
    Monta um arquivo .json a partir de um dicionario.

    :param dict: Dicionario com o que sera escrito
    :param nome: Nome do arquivo .json que sera escrito.
    :return: (boolean)
    """
    # faz no maximo n tentativas de escrita
    for i in range(30):
        try:
            # print("[jsonWrite.gravaJson]", "tentativa de escrita num.", i+1, "em", nome)
            with open(nome, 'w') as arq:
                json.dump(dict, arq)
            return True
        except PermissionError:
            # Esta em uso pelo sistema, tento novamente
            pass
    return False

# ------------------------------ TESTE ------------------------------
# FUNCIONANDO

# d = {"teste":1, "teste2":2}
# NOME_ARQ = os.path.join("data", "testeJsonWrite.json")
# gravaJson(dict = d, nome = NOME_ARQ)
