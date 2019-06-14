from flask import Flask, jsonify, json, request, render_template
from flask_cors import CORS
import c
app = Flask(__name__)
CORS(app)

with open("league.json", "r") as read_file:
    league = json.load(read_file)
    ip = league["ip"]

@app.route("/", methods=['GET'])
def getJson():
    with open("league.json", "r") as read_file:
        league = json.load(read_file)
        ip = league["ip"]
    c.send('20', '-1',  '127.0.0.2', '127.0.0.1', '127.0.0.3')
    return jsonify(league)

@app.route("/teste", methods=['GET'])
def getLat():
    return ('chamar metodo acima')


if __name__ == '__main__':
    app.run(host=ip, port=5000)