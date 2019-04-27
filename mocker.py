import json
from random import *
from time import sleep

with open("route.json", "r") as read_file:
    route = json.load(read_file)

#MOCKER DOS SENSORES:
def lat_log(x):
    if x < 0:
        x *= -1
    i = 0
    s = choice([-1, 1])
    while i == 0:
        i = randrange(x+5)
    return i*s

def Latitude(mov, ms, mn, ):
    if not mov:
        print("Estavel")
        if not ms or not mn:
            #Latitude Simular
            novaLat = lat_log(10)
            if (route["maxLatitude"]+route["latitude"]) < novaLat or (route["maxLatitude"]-route["latitude"]) > novaLat:
                route["movimento"] = True
                if novaLat > route["maxLatitude"]:
                    ms = True
                else:
                    mn = True

        return novaLat

    else:
        print("Instavel")
        #Norte ou Sul

        #Muito Norte - Ligar motorS
        novaLat = 0
        if route["motorS"]:
            novaLat = route["latitude"] - 1
            if novaLat == route["latP"] + route["maxLatitude"]:
                route["motorS"] = False
                route["movimento"] = False

        #Muito Sul - Ligar motorN
        if route["motorN"]:
            novaLat = route["latitude"] + 1
            if novaLat == route["latP"] - route["maxLatitude"]:
                route["motorN"] = False
                route["movimento"] = False

        return novaLat

def Longitude():
    pass

def Altitude():
    pass

while True:
    route["latitude"] = Latitude()
    #route["altitude"] = Altitude()
    with open('route.json', 'w') as outfile:  
        json.dump(route, outfile)
    
    print(route["latitude"],"-",route["movimento"])
    sleep(2)

#{"sistema": true, "ip": "127.0.0.1", "mascara": "127.0.0.0", "porta": 4500, "status": 200, "dbs": 10, "conectado": "127.0.0.2", "latitude": 2, "maxLatitude": 2, "longitude": 2, "maxLongitude": 2, "altitude": 1, "maxAltitude": 100,"movimento": false, "latP": 2, "longP": 2, "motorN": false, "motorS": false, "motorL": false, "motorO": false, "motorUp": true, "motorDown": false,"modo": "slave"}