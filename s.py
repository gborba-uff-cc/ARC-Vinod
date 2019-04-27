import socket, json
import threading

with open("route.json", "r") as read_file:
    route = json.load(read_file)

class Server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    connections = []
    print("Server pronto...")
    def __init__(self): 
        self.sock.bind((route["ip"],route["porta"])) 
        self.sock.listen(1) 

    def handler(self, c, a):
        while True:
            data = c.recv(1024)
            if not data:
                print("D",str(a[0])," ",str(a[1]))
                self.connections.remove
            else:
                data = str(data, 'utf-8')
                jsonRead(data)
                #print(data)


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

    def jsonRead(self, x):
        #Alterar o JSON
        if x == '1':
            print('caso 1')
        
        #Desconecar
        elif == '2':
            print('caso 2')
        
        else:
            print('comando não existe')

server = Server()
server.run()