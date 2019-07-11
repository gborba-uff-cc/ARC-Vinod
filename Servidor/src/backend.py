from flask import Flask, jsonify, json, request, render_template
from flask_cors import CORS
import c
import os
app = Flask(__name__)
CORS(app)


data= { 
    "ip": "127.0.0.1",  
    "conectado": "127.0.0.2", # na nossa aplicacao vai ser o conectando.
    "conectando" : ["127.0.0.-1, 127.0.0.-1"], # valores default para teste que na vdd nao vao ser usados
    "mascara" : "127.0.0.0",   
    "porta": 4500, 
    "status": 200, 
    "dbs": 10, 
    "latitude": -0, 
    "longitude": -0,
    "altitude": -0, 
    "movimento": True,
    "modo": "undefined", 
    }




@app.route("/<int:id>", methods=['GET'])
def getJson(id):

    if os.path.exists("./data/127.0.0."+str(id+1)+".json") == False:
        with open ("./data/127.0.0."+str(id+1)+".json", "w") as f:
            json.dump(data, f)

    with open("./data/127.0.0."+str(id+1)+".json", "r") as read_file:
        league = json.load(read_file)

    return jsonify(league)

@app.route("/get<string:input><int:id>", methods=['GET'])
def getInfo(input, id):
    print ("id = ", id)
    with open("./data/127.0.0."+str(id+1)+".json", "r") as read_file:
        league = json.load(read_file)
    if league["modo"] == "slave":
        destino = league["conectado"]
    else:
        destino = league["ip"]
    if input == 'lat':
        print ("destino = ", destino)
        c.send('120', 'lat -999',  destino, '127.0.0.1', league["ip"])
    if input == 'long':
        c.send('120', 'long -999',  destino, '127.0.0.1', league["ip"])
    if input == 'alt':
        c.send('120', 'alt -999',  destino, '127.0.0.1', league["ip"])
          
    return ("")

@app.route("/send<string:input><int:id>", methods=['GET'])
def sendInfo(input, id):
    print ("id = ", id)
    temp = input.split()
    with open("./data/127.0.0."+str(id+1)+".json", "r") as read_file:
        league = json.load(read_file)
    if league["modo"] == "slave":
        destino = league["conectado"]
    else:
        destino = league["ip"]
    if temp[0] == 'lat':
        print ("destino = ", destino, "info = ", temp[1])
        c.send('220', 'lat '+str(temp[1]),  destino, '127.0.0.1', league["ip"])
    if temp[0] == 'long':
        c.send('220', 'long '+str(temp[1]),  destino, '127.0.0.1', league["ip"])
    if temp[0] == 'alt':
        c.send('220', 'alt '+str(temp[1]),  destino, '127.0.0.1', league["ip"])
    return("")


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)