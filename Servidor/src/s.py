import socket, json
import threading

with open("./data/infosRoteador.json", "r") as read_file:
    route = json.load(read_file)

class Server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    connections = []
    #print("Server pronto...")
    def __init__(self): 
        #self.sock.bind((route["ip"],route["porta"])) 
        self.sock.bind(("127.0.0.1",route["porta"]))
        print("Server pronto...")
        self.sock.listen(1) 

    def handler(self, c, a):
        while True:
          
            cod, info, origem, destinoFinal = [str(i) for i in c.recv(2048).decode('utf-8').split('\n')]
            
            if not cod:
                print("D",str(a[0])," ",str(a[1]))
                self.connections.remove
            else:
                import c as cliente
                import jsonRead as jr


#----------------------------- MENSAGEIROS --------------------------------------------------------------------------------------------
                if (cod == '11'):
                    if ("127.0.0.1" != origem):
                        print('master recebeu de volta')
                        cliente.send ('11', info, origem, origem, destinoFinal)
                        c.close
                    else:
                        print('server recebeu de volta')
                        print(info)
                        c.close

                elif (cod == '20'):  
                    if (destinoFinal == jr.getIp() and jr.getType()): #pegar o propio ip
                        print('slave recebeu')
                        cliente.send ('11', jr.getLatitude(), jr.getMasterIp(), origem, destinoFinal) #ler location do json
                        c.close
                    elif (destinoFinal == jr.getIp()): #pegar o propio ip
                        cliente.send ('11', jr.getLatitude(), origem, origem, destinoFinal) #ler location do json
                        c.close
                    else:
                        print ('balao mestre recebeu')
                        cliente.send ('20', info, destinoFinal, origem, destinoFinal)
                        c.close  
#----------------------------------------------------------------------------------------------------------------------------------------
                
                else:
                    print('comando nao existe')
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
