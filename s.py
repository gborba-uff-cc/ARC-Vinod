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
            cod, info = [str(i) for i in c.recv(2048).decode('utf-8').split('\n')]
            
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

                elif cod == '11':
                    #escrever direto no json (seria algo que so o servidor do react pode fazer)
                    c.close

                elif cod == '20': #caso de envio de latitude para o ''servidor''
                    import c as cliente
                    #ler do json e enviar para endereco original
                    #cliente.send ('11', 'valor lido do json', 'endecreco lido do original' ) #formular logica para: se for slave mandar para o mestre primeiro
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