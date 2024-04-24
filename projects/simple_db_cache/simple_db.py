from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
cache = {}
MAX_CACHE_SIZE = 10

def get_db_connection():
    conn = sqlite3.connect('urls.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT UNIQUE NOT NULL  
        )
    ''')
    conn.commit()
    conn.close()

def add_to_cache(key, value):
    global cache
    if len(cache) >= MAX_CACHE_SIZE:
        # Evict the oldest item (FIFO for simplicity)
        cache.pop(next(iter(cache)))
    cache[key] = value

@app.route('/urls', methods=['POST'])
def create_url():
    data = request.json
    original_url = data.get('url')

    # Check cache first to avoid unnecessary DB access
    for key, value in cache.items():
        if value == original_url:
            return jsonify({"id": key, "original_url": value}), 200

    conn = get_db_connection()
    cursor = conn.cursor()

    # Check if the URL already exists in the database
    result = cursor.execute('SELECT id FROM urls WHERE original_url = ?', (original_url,)).fetchone()
    if result:
        conn.close()
        return jsonify({"id": result['id'], "original_url": original_url}), 200

    # If not, insert new URL into the database
    try:
        cursor.execute('INSERT INTO urls (original_url) VALUES (?)', (original_url,))
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        add_to_cache(new_id, original_url)  # Add new URL to cache
        return jsonify({"success": True, "id": new_id}), 201
    except sqlite3.IntegrityError:  # Catch uniqueness constraint violation
        conn.close()
        return jsonify({"error": "URL already exists"}), 409

@app.route('/urls/<int:id>', methods=['GET'])
def get_url(id):
    # Check cache first
    if id in cache:
        return jsonify({"id": id, "original_url": cache[id]})

    # If not in cache, query the database
    conn = get_db_connection()
    url = conn.execute('SELECT * FROM urls WHERE id = ?', (id,)).fetchone()
    conn.close()
    if url is None:
        return jsonify({"error": "Not found"}), 404
    
    # Add to cache before returning
    add_to_cache(url['id'], url['original_url'])
    return jsonify({"id": url['id'], "original_url": url['original_url']})

init_db()  # Ensure the database is initialized before starting the app
app.run()

