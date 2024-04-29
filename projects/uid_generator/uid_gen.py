from flask import Flask, jsonify, request
import uuid
import sqlite3
import random
import string
import hashlib
import time

app = Flask(__name__)

def init_db():
    with app.app_context():
        db = get_db()
        db.execute('CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY)')
        db.commit()

def get_db():
    db = sqlite3.connect('app.db')
    db.row_factory = sqlite3.Row
    return db

@app.route('/')
def home():
    return "Welcome to the Unique ID Generator Service"

# Generate UUID
@app.route('/generate/uuid', methods=['GET'])
def generate_uuid():
    id = uuid.uuid4().hex
    return jsonify({'uuid': id})

# Generate Incremental ID
@app.route('/generate/incremental', methods=['GET'])
def generate_incremental():
    db = get_db()
    cursor = db.execute('INSERT INTO items (id) VALUES (NULL)')
    db.commit()
    id = cursor.lastrowid
    db.close()
    return jsonify({'incremental_id': id})

# Generate Short Alphanumeric ID
@app.route('/generate/short', methods=['GET'])
def generate_short_id():
    length = request.args.get('length', default=6, type=int)
    characters = string.ascii_letters + string.digits
    id = ''.join(random.choice(characters) for _ in range(length))
    return jsonify({'short_id': id})

# Generate Hash ID
@app.route('/generate/hash', methods=['POST'])
def generate_hash_id():
    data = request.json.get('data', '')
    unique_input = data + str(time.time())
    id = hashlib.sha256(unique_input.encode()).hexdigest()
    return jsonify({'hash_id': id})

init_db()
app.run(debug=True)
