import hashlib
from flask import Flask, request, jsonify, redirect

app = Flask(__name__)

# List of object storage nodes
nodes = {
    'object_storage_1': 'http://object_storage_1:5000',
    'object_storage_2': 'http://object_storage_2:5000',
    'object_storage_3': 'http://object_storage_3:5000',
}

# Simple consistent hashing implementation
def get_node(key):
    hash_value = int(hashlib.md5(key.encode()).hexdigest(), 16)
    node_keys = sorted(nodes.keys())
    return nodes[node_keys[hash_value % len(node_keys)]]

@app.route('/store', methods=['POST'])
def store():
    key = request.json['key']
    node_url = get_node(key)
    response = redirect(f'{node_url}/store', code=307)
    return response

@app.route('/retrieve/<key>', methods=['GET'])
def retrieve(key):
    node_url = get_node(key)
    response = redirect(f'{node_url}/retrieve/{key}', code=307)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

