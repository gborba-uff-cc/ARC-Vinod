from flask import Flask, jsonify, json, request, render_template

app = Flask(__name__)

with open("route.json", "r") as read_file:
    route = json.load(read_file)
    ip = route["ip"]
    con = route["conectado"]

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/teste')
def register():
    result = {
        "status": "200"
    }

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host=ip, port=5000)