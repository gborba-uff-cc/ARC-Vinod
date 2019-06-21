import socket, json
import threading
import os

with open("./data/infosRoteador.json", "r") as read_file:
    route = json.load(read_file)

class Server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    connections = []
    # nome do arquivo que este server usa para sinalizar ao balao
    NOME_ARQUIVO_FLAGS_SERVER = os.path.join("data","flagsServer.json")
    # nome do arquivo que este server passar valores ao balao
    NOME_ARQUIVO_POSICAO_ALVO = os.path.join("data","posicionamentoServer.json")
    #print("Server pronto...")
    def __init__(self): 
        #self.sock.bind((route["ip"],route["porta"])) 
        self.sock.bind((route["ip"],route["porta"]))
        print("Server pronto...") 
        self.sock.listen(1) 

    def handler(self, c, a):
        while True:
          
            cod, info, origem, destinoFinal = [str(i) for i in c.recv(2048).decode('utf-8').split('\n')]
            
            if not cod:
                print("D",str(a[0])," ",str(a[1]))
                self.connections.remove()
            else:
                import c as cliente
                import jsonRead as jr
                import jsonWrite as jw


#----------------------------- MENSAGEIROS DE LEITURA (NA VISAO DO SERVIDOR) -------------------------
                if (cod == '110'):
                    if (jr.getIp() != origem):
                        print('master recebeu de volta')
                        cliente.send ('110', info, origem, origem, destinoFinal)
                        c.close()
                    else:
                        print('server recebeu de volta')
                        print(info)
                        # escrever aqui no json do servidor
                        c.close()

                elif (cod == '120'):  
                    if (destinoFinal == jr.getIp() and jr.getType() == 'slave'): 
                        print('slave recebeu')
                        cliente.send ('110', jr.getLatitude(), jr.getMasterIp(), origem, destinoFinal) #ler location do json
                        c.close()
                    elif (destinoFinal == jr.getIp()): #pegar o propio ip
                        cliente.send ('110', jr.getLatitude(), origem, origem, destinoFinal) #ler location do json
                        c.close()
                    else:
                        print ('balao mestre recebeu')
                        cliente.send ('120', info, destinoFinal, origem, destinoFinal)
                        c.close()
#--------------------------------------------------------------------------------------------------------------

#----------------------------- MENSAGEIROS DE ESCRITA ----------------------------------------------------------
                elif (cod == '210'):
                    if (jr.getIp() != origem):
                        print('master recebeu de volta')
                        cliente.send ('210', info, origem, origem, destinoFinal)
                        c.close()
                    else:
                        print('server recebeu de volta')
                        print(info)
                        c.close()

                elif (cod == '220'):  
                    if (destinoFinal == jr.getIp() and jr.getType() == 'slave'): #pegar o propio ip
                        print('slave recebeu')
                        # TODO escrever no json aqui
                        # dizer ao balão que vai atualizar a posição alvo
                        if self.sinalizaMudancaAlvo(True):
                        # atualizar a posição alvo
                            # carregar o json atual
                            d = jr.carregaJson(self.NOME_ARQUIVO_POSICAO_ALVO)
                            # atualizar o json
                            d["alvoLatitude"] = 50  # TODO tirar a constante daqui
                            # gravar o json novamente
                            jw.gravaJson(d, self.NOME_ARQUIVO_POSICAO_ALVO)
                            # dizer que ja atualizou a posição alvo
                            self.sinalizaEscritaJson(False)
                        else:
                            # TODO mensagem de não ok
                            pass

                        # if (testarleitura()):
                        #   escreverLatitudeJson(info)
                        cliente.send ('210', 'ok', jr.getMasterIp(), origem, destinoFinal)
                        c.close()
                    elif (destinoFinal == jr.getIp()): #pegar o propio ip
                        cliente.send ('210', jr.getLatitude(), origem, origem, destinoFinal) #ler location do json
                        c.close()
                    else:
                        print ('balao mestre recebeu')
                        cliente.send ('220', info, destinoFinal, origem, destinoFinal)
                        c.close()
#-------------------------------------------------------------------------------------------------------------------------
                else:
                    print('comando nao existe')
                    c.close()
            break

    def sinalizaEscritaJson(self, val):
        """
        Sinaliza ao balao, com o valor recebido, o inicio ou o fim da modificação na posição alvo
        :param val: (boolean)
        :return:
        """
        import jsonRead
        import jsonWrite
        d = jsonRead.carregaJson(self.NOME_ARQUIVO_FLAGS_SERVER)
        if d is not None:
            d["modificandoPosicionamentoAlvo"] = val
            jsonWrite.gravaJson(d, self.NOME_ARQUIVO_FLAGS_SERVER)
            return True
        else:
            return False

    
    def run(self):
        while True:
            c,a = self.sock.accept() 
            cThread = threading.Thread(target=self.handler, args=(c,a)) 
            cThread.daemon = True 
            cThread.start() 
            self.connections.append(c) 
            print("C",str(a[0])," ",str(a[1]))

server = Server()
server.run()
