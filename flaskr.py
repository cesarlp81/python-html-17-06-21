import sqlite3
from flask import Flask, g

# Configurações

DATABASE = './flaskr.db'
SECRET_KEY = "pudim"
USERNAME = 'admin'
PASSWORD = 'admin'

# aplicação

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(DATABASE)

@app.before_request
def before():
    g.db = connect_db()

@app.teardown_request
def after(exception):
    g.db.close()

@app.route('/')
def index():
    return "<h1>Hello World</h1>"