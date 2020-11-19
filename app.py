from fernet import Fernet
from flask import Flask, render_template, request


app = Flask(__name__)
key = Fernet.generate_key()
f = Fernet(key)

@app.route('/')
@app.route('/<name>')
def index(name='Name'):
    title = request.args.get('title', 'default')
    return render_template('index.html', name=name, title=title)

@app.route('/encrypt')
def string_to_encrypt_method():
    title = request.args.get('param', 'default')
    token = f.encrypt(title)
    return render_template('index.html', name=token, title=title)


@app.route('/decrypt')
def string_to_decrypt_method():
    title = request.args.get('param', 'default')
    dec = f.decrypt(title)
    return render_template('index.html', name=dec, title=title)

@app.route('/catalog')
def catalog():
    return "catalog!!!"

app.run(debug=True, port=5009)