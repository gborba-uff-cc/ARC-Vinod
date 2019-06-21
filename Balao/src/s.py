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
    # equivalencia para os campos nos jsons
    equivAlvoLatitude = {"lat", "latitude", "latitudealvo", "alvolatitude"}
    equivAlvoLongitude = {"long", "longitude", "longitudealvo","alvolongitude"}
    equivAlvoAltura = {"alt", "altura", "alturaalvo", "alvoaltura"}
    equivDesvioLatitude = {"dlat", "desviolatitude", "desviolatitudealvo", "desvioalvolatitude"}
    equivDesvioLongitude = {"dlong", "desviolongitude", "desviolongitudealvo","desvioalvolongitude"}
    equivDesvioAltura = {"dalt", "desvioaltura", "desvioalturaalvo", "desvioalvoaltura"}
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
                # TODO remove precisa de parametro(s)
                self.connections.remove
            else:
                import c as cliente
                import jsonRead as jr
                import ManipuladorServerBalao as arq_msb
                manipulador = arq_msb.ManipuladorServerBalao()


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
                        possivel = True
                        temp = info.split()
                        temp[1] = int(temp[1])
                        # se a informação tem dois campos e consegui dizer ao balão que vai atualizar a posição alvo
                        if len(temp) == 2 and manipulador.atualizaCampoJson(self.NOME_ARQUIVO_FLAGS_SERVER,
                                                                            modificandoPosicionamentoAlvo=True):
                            # escreve nova(o) latitude
                            if temp[0].lower() in self.equivAlvoLatitude:
                                manipulador.atualizaCampoJson(self.NOME_ARQUIVO_POSICAO_ALVO,
                                                              alvoLatitude=temp[1])
                            # escreve nova(o) longitude
                            elif temp[0].lower() in self.equivAlvoLongitude:
                                manipulador.atualizaCampoJson(self.NOME_ARQUIVO_POSICAO_ALVO,
                                                              alvoLongitude=temp[1])
                            # escreve nova(o) altura
                            elif temp[0].lower() in self.equivAlvoAltura:
                                manipulador.atualizaCampoJson(self.NOME_ARQUIVO_POSICAO_ALVO,
                                                              alvoAltura=temp[1])
                            # escreve nova(o) desvio latitude
                            elif temp[0].lower() in self.equivDesvioLatitude:
                                manipulador.atualizaCampoJson(self.NOME_ARQUIVO_POSICAO_ALVO,
                                                              desvioLatitude=temp[1])
                            # escreve nova(o) desvio longitude
                            elif temp[0].lower() in self.equivDesvioLongitude:
                                manipulador.atualizaCampoJson(self.NOME_ARQUIVO_POSICAO_ALVO,
                                                              desvioLongitude=temp[1])
                            # escreve nova(o) desvio altura
                            elif temp[0].lower() in self.equivDesvioAltura:
                                manipulador.atualizaCampoJson(self.NOME_ARQUIVO_POSICAO_ALVO,
                                                              desvioAltura=temp[1])
                            else:
                                possivel = False
                            # diz que terminou de atualizar a posição alvo
                            manipulador.atualizaCampoJson(self.NOME_ARQUIVO_FLAGS_SERVER,
                                                          modificandoPosicionamentoAlvo=False)
                        else:
                            possivel = False
                        if possivel:
                            cliente.send ('210', 'ok', jr.getMasterIp(), origem, destinoFinal)
                        else:
                            cliente.send ('210', 'nao ok', jr.getMasterIp(), origem, destinoFinal)
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
