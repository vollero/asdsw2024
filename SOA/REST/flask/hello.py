from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!\n'

@app.route('/ita')
def hello_ita():
    return 'Ciao a tutti!\n'
