import socket, json
import sys

# cod - descreve qual o tipo da requisicao..
# para entendimento humano : primeiro digito se refere a leitura/escrita, o resto representa a funcao 
# cod - 10 - servidor quer enviar latitude desejada para ser escrita em latP de algum balao.
# cod - 11 - envio exclusivo de um balao (mandar para escrever direto no latidude no jason do servidor)
# cod - 20 - servidor pediu a latitude apesar de mandarmos o cod e o info, nesse caso o info pouco importa

def send(cod, info , destino, origem, destinoFinal):
    with open("route.json", "r") as read_file:
        route = json.load(read_file)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.connect((route["ip"],route["porta"])) 
    s.connect((destino,route["porta"]))
    #print("Cliente pronto...")
    s.sendall(str.encode("\n".join([str(cod), str(info), str(origem), str(destinoFinal)])))
    
