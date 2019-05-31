with open("route.json", "r") as read_file:
        route = json.load(read_file)

def getIp():
    with open("route.json", "r") as read_file:
        route = json.load(read_file)
    
    return route["ip"]