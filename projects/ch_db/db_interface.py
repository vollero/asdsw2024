from flask import Flask, request, jsonify
import requests
import hashlib

app = Flask(__name__)

servers = [
    "http://localhost:6000/",
    "http://localhost:6001/",
    "http://localhost:6002/"
]

def hash_function(key):
    return int(hashlib.md5(key.encode()).hexdigest(), 16)

def get_server(key):
    server_hashes = {hash_function(server+'1'): server for server in servers}
    for i in range(2,10):
        server_hashes.update({hash_function(server+str(i)): server for server in servers})
   
    sorted_hashes = sorted(server_hashes.keys())
    
    key_hash = hash_function(key)
    
    for server_hash in sorted_hashes:
        if key_hash < server_hash:
            return server_hashes[server_hash]
    
    return server_hashes[sorted_hashes[0]]

@app.route('/get/<int:key>', methods=['GET'])
def get(key):
    server_url = get_server(str(key)) + 'get/' + str(key)

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
    r = requests.post(get_server(str(key)) + 'put', json=d, headers=h)
    return d

if __name__ == '__main__':
    app.run(debug=True)

