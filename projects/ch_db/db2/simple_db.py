from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('keyvalue.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS keyvalue (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT UNIQUE NOT NULL,
            value TEXT NOT NULL  
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/put', methods=['POST'])
def put():
    data = request.json
    key  = data.get('key')
    value = data.get('value')

    conn = get_db_connection()
    cursor = conn.cursor()

    # Check if the URL already exists in the database
    result = cursor.execute('SELECT value FROM keyvalue WHERE key = ?', (key,)).fetchone()
    if result:
        conn.close()
        return jsonify({"success": False, "key": key, "value": result['value']}), 200

    # If not, insert new URL into the database
    try:
        cursor.execute('INSERT INTO keyvalue (key, value) VALUES (?,?)', (key, value,))
        conn.commit()
        conn.close()
        return jsonify({"success": True, "key": key, "value": value}), 201
    except sqlite3.IntegrityError:  # Catch uniqueness constraint violation
        conn.close()
        return jsonify({"error": "URL already exists"}), 409

@app.route('/get/<int:key>', methods=['GET'])
def get(key):
    # If not in cache, query the database
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM keyvalue WHERE key = ?', (key,)).fetchone()
    conn.close()
    if data is None:
        return jsonify({"error": "Not found"}), 404

    return jsonify({"key": data['key'], "value": data['value']})

init_db()  # Ensure the database is initialized before starting the app
app.run()

