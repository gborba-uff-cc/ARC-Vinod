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
        self.sock.bind(('127.0.0.3',route["porta"]))
        print("Server pronto...") 
        self.sock.listen(1) 

    def handler(self, c, a):
        while True:
            data = c.recv(1024)
            if not data:
                print("D",str(a[0])," ",str(a[1]))
                self.connections.remove
            else:
                data = str(data, 'utf-8')

                #Tratamento o JSON
                if data == '1':
                    import c as client
                    print('caso 1')
                    client.send('2', '127.0.0.3')
                    c.close
                
                #Desconecar
                elif data == '2':
                    print('caso 2')
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