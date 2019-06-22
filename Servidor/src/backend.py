from flask import Flask, jsonify, json, request, render_template
from flask_cors import CORS
import c
import os
app = Flask(__name__)
CORS(app)


data= { 
    "ip": "127.0.0.1", 
    "mascara": "127.0.0.0", 
    "porta": 4500, 
    "status": 200, 
    "dbs": 10, 
    "conectado": "127.0.0.2",
    "latitude": -0, 
    "longitude": -0,
    "altitude": -0, 
    "maxAltitude": 100,
    "movimento": True,
    "latP": 1, 
    "longP": 1, 
    "modo": "slave", 
    "altP": 1
    }




@app.route("/<int:id>", methods=['GET'])
def getJson(id):

    if os.path.exists("./data/127.0.0."+str(id+1)+".json") == False:
        with open ("./data/127.0.0."+str(id+1)+".json", "w") as f:
            json.dump(data, f)

    with open("./data/127.0.0."+str(id+1)+".json", "r") as read_file:
        league = json.load(read_file)

    #c.send('220', 'lat -999',  '127.0.0.2', '127.0.0.1', '127.0.0.3')

    return jsonify(league)

@app.route("/teste", methods=['GET'])
def getLat():
    return ('chamar metodo acima')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)