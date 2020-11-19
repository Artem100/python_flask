from fernet import Fernet
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name='Name'):
    title = request.args.get('title', 'default')
    return render_template('index.html', name=name, title=title)

@app.route('/encrypt?string=<string_to_encrypt>')
@app.route('/<string_to_encrypt>')
def string_to_encrypt_method(name='string_to_encrypt'):
    title = request.args.get('title', 'default')
    return render_template('index.html', name=name, title=title)

@app.route('/decrypt?string=<string_to_decrypt>')
@app.route('/<name>')
def string_to_encrypt_method(name='string_to_decrypt'):
    title = request.args.get('title', 'default')
    return render_template('index.html', name=name, title=title)

@app.route('/catalog')
def catalog():
    return "catalog!!!"

app.run(debug=True, port=5005)