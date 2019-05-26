import socket, json
import sys

def send(msg, destino):
    with open("route.json", "r") as read_file:
        route = json.load(read_file)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.connect((route["ip"],route["porta"])) 
    s.connect((destino,route["porta"]))
    #print("Cliente pronto...")
    m = msg
    print(m)
    s.send(bytes(m, 'utf-8'))