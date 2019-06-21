import jsonRead
import jsonWrite
# import os  # TESTE


class ManipuladorServerBalao:

    def __init__(self):
        pass

    def atualizaCampoJson(self, arq, **kwargs):
        """
        Atualiza o(s) campo(s) no(s) arquivo(s) com o(s) valor(es) que foram recebidos na forma.

        :param arq: nome do arquivo que sera aberto
        :param kwargs: campo=valor  <- forma de uso;
                       campo é o parametro que corresponde ao campo que sera atualizado;
                       valor é o novo valor para o campo;
        :return: (boolean) dizendo se a atualização do valor foi bem sucedida
        """
        d = jsonRead.carregaJson(arq)
        if d is not None:
            for c, v in kwargs.items():
                d[c] = v
            jsonWrite.gravaJson(d, arq)
            return True
        else:
            return False
