from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Prueba de la aplicación</h1>'
@app.route('/user/<name>')
def user(name):
    return '<h1>Hola, {}!</h1>'.format(name)