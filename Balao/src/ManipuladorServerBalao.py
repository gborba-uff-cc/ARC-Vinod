import jsonRead
import jsonWrite
# import os  # TESTE


class ManipuladorServerBalao:

    def __init__(self):
        pass

    def atualizaCampoJson(self, arq, **kwargs):
        """
        Atualiza o(s) campo(s) no arquivo com o(s) valor(es) que foram recebidos.

        :param arq: nome do arquivo que sera aberto
        :param kwargs: campo=valor, ...
            -> Forma de uso:
                campo e` o parametro que corresponde ao campo que sera atualizado;
                valor e` o novo valor para o campo;
        :return: (boolean) dizendo se a atualizacao do valor foi bem sucedida
        """
        d = jsonRead.carregaJson(arq)
        if d is not None:
            for c, v in kwargs.items():
                d[c] = v
            jsonWrite.gravaJson(d, arq)
            return True
        else:
            return False


# ------------------------------ TESTE ------------------------------
# funcionando

# ManipuladorServerBalao().atualizaCampoJson(arq=os.path.join("data","flagsServer.json"),
#                                            sistema=False,
#                                            lendoDadosPosicionamento=False,
#                                            modificandoPosicionamentoAlvo=False)
