from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# List of backend servers
servers = [
    #"http://localhost:6000/",
    #"http://localhost:6001/",
    "http://localhost:6002/"
]

current_server = 0

def get_server(key):
    #
    # implement here the sharding logic
    #
    global current_server
    server = servers[current_server]
    current_server = (current_server + 1) % len(servers)
    return server

@app.route('/get/<int:key>', methods=['GET'])
def get(key):
    server_url = get_server(key) + 'get/' + str(key)
    try:
        response = requests.get(server_url)
        if response.status_code == 200:
            result = response.json()
            result['server'] = server_url
            return jsonify(result), 200
        else:
            return jsonify({'error': 'Failed to get the (key,value) element', 'server': server_url}), 500
    except requests.exceptions.RequestException:
        return jsonify({'error': 'Backend server error', 'server': server_url}), 500


@app.route('/put', methods=['POST'])
def put():
    d = request.json
    key = d["key"]
    h = {'Content-Type': 'application/json'};
    r = requests.post(get_server(key) + 'put', json=d, headers=h)
    return d

if __name__ == '__main__':
    app.run(debug=True)

