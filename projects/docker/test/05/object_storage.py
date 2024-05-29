from flask import Flask, request, jsonify

app = Flask(__name__)
storage = {}

@app.route('/store', methods=['POST'])
def store():
    key = request.json['key']
    value = request.json['value']
    storage[key] = value
    return jsonify({'status': 'stored', 'key': key, 'value': value})

@app.route('/retrieve/<key>', methods=['GET'])
def retrieve(key):
    value = storage.get(key)
    if value:
        return jsonify({'status': 'found', 'key': key, 'value': value})
    else:
        return jsonify({'status': 'not found', 'key': key}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

