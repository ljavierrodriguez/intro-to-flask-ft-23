import json
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def main():
    msg = {
        "message" : "Hola Mundo desde Flask"
    }
    return jsonify(msg)


@app.route('/status', methods=['POST'])
def get_status():
    return "Status"

@app.route('/registrar', methods=['POST', 'PUT'])
def registrar():
    
    if request.method == 'POST':
        print("POST")

    if request.method == 'PUT':
        print("PUT")
    
    #data_json = json.loads(request.data)
    data_json = request.get_json()
    
    print(data_json["name"])
    
    return jsonify(data_json)
    
    
@app.route('/saludar/<name>/<lastname>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def saludar(name, lastname):
    
    return jsonify({ "name": name, "lastname": lastname })


@app.route('/users', methods=['GET'])
def users():
    
    params = request.args
    
    print(params['limit'])
    
    return jsonify({ "users": "users"})
    

if __name__ == "__main__":
    app.run()