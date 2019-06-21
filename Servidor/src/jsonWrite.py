import json
# import os  # TESTE


def gravaJson(dict, nome):
    """
    Monta um arquivo .json a partir de um dicionário.

    :param dict: Dicionário com o que será escrito
    :param nome: Nome do arquivo .json que será escrito.
    :return: (boolean)
    """
    # faz no maximo n tentativas de escrita
    for i in range(30):
        try:
            print("[jsonWrite.gravaJson]", "tentativa de escrita num.", i+1)
            with open(nome, 'w') as arq:
                json.dump(dict, arq)
            return True
        except PermissionError:
            # Está em uso pelo sistema, tento novamente
            pass
    return False

# ------------------------------ TESTE ------------------------------
# FUNCIONANDO

# d = {"teste":1, "teste2":2}
# NOME_ARQ = os.path.join("data", "testeJsonWrite.json")
# gravaJson(dict = d, nome = NOME_ARQ)
