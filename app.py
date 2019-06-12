from flask import Flask, jsonify, json, request, render_template
from flask_cors import CORS
import sys

app = Flask(__name__)
CORS(app)

with open("./src/data/infosRoteador.json", "r") as read_file:
    infosRoteador = json.load(read_file)

ip = infosRoteador["ip"]
porta = infosRoteador["porta"]
#print(ip, porta)

@app.route("/")
def App():
    with open("./src/data/dadosPosicionamento.json", "r") as read_file:
        dadosPosicionamento = json.load(read_file)
    
    return jsonify(dadosPosicionamento)

if __name__ == '__main__':
    app.run(host=ip, port=porta)