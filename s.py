import socket, json
import threading

with open("route.json", "r") as read_file:
    route = json.load(read_file)

class Server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    connections = []
    #print("Server pronto...")
    def __init__(self): 
        #self.sock.bind((route["ip"],route["porta"])) 
        self.sock.bind(('127.0.0.4',route["porta"]))
        print("Server pronto...") 
        self.sock.listen(1) 

    def handler(self, c, a):
        while True:
          
            cod, info, origem, destinoFinal = [str(i) for i in c.recv(2048).decode('utf-8').split('\n')]
            
            if not cod:
                print("D",str(a[0])," ",str(a[1]))
                self.connections.remove
            else:

                #Tratamento o JSON
                ####-------MENSAGEIROS-------###
                if cod == '10': #caso de envio de latitude desejada (pensar em alguma forma para o caso desse ainda nao ser o balao correto para receber)
                    print(cod)
                    print(info)
                     # abrir o jason para escrita da info 
                    c.close
                   
                
                #Desconecar
                
                ######################### PIPELINE DE QUALQUER REQUISICAO ###########################
                #FALTA IMPLEMENTAR get.location()
                #FALTA IMPLEMENTAR get.master_ip()
                #FALTA IMPLEMENTAR get.ip()
                # Podemos reusar o codigo para qualquer outro tipo de requisicao alem da location

                elif cod == '11':
                    if (get.ip() != origem):
                        c.send ('11', info, origem, origem, destinoFinal)
                    else:
                        pass
                        #abre jason
                        #escreve location
                        #fecha json
                    c.close

                elif cod == '20':
                    import c as cliente
                    import jsonRead as jr
                    if (destinoFinal == jr.getIp() and get.status() == 'slave'): #pegar o propio ip
                        c.send ('11', get.location(), get.master_ip(), origem, destinoFinal) #ler location do json
                        c.close
                    elif (destinoFinal == get.ip()): #pegar o propio ip
                        c.send ('11', get.location(), origem, origem, destinoFinal) #ler location do json
                        c.close
                    else:
                        c.send ('20', info, destinoFinal, origem, destinoFinal)
                    print (cod)
                    print (info)
                    c.close
                
                else:
                    print('comando não existe')
                    c.close
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