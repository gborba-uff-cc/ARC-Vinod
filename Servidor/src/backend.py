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
    "modo": "undefined", 
    "altP": 1
    }




@app.route("/<int:id>", methods=['GET'])
def getJson(id):

    if os.path.exists("./data/127.0.0."+str(id+1)+".json") == False:
        with open ("./data/127.0.0."+str(id+1)+".json", "w") as f:
            json.dump(data, f)

    with open("./data/127.0.0."+str(id+1)+".json", "r") as read_file:
        league = json.load(read_file)


    return jsonify(league)

@app.route("/get<string:input>", methods=['GET'])
def getInfo(input):
    print (input)
    if input == 'lat':
        c.send('120', 'lat -999',  '127.0.0.2', '127.0.0.1', '127.0.0.3')
    if input == 'long':
        c.send('120', 'long -999',  '127.0.0.2', '127.0.0.1', '127.0.0.3')
    if input == 'alt':
        c.send('120', 'alt -999',  '127.0.0.2', '127.0.0.1', '127.0.0.3')
          
    return ("")


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)