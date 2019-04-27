import socket, json

with open("route.json", "r") as read_file:
    route = json.load(read_file)
print("Cliente pronto...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((route["ip"],route["porta"])) 
m = input("")
s.send(bytes(m, 'utf-8'))