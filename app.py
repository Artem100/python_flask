from fernet import Fernet
from flask import Flask, render_template, request


app = Flask(__name__)
key = Fernet.generate_key()
f = Fernet(key)

@app.route('/encrypt')
def string_to_encrypt_method():
    title = request.args.get('param', 'default')
    token = f.encrypt(title)
    return render_template('index.html', name=token, title=title)


@app.route('/decrypt')
def string_to_decrypt_method():
    title_dec = request.args.get('param', 'default')
    list_title = list(title_dec)
    new_list = []
    for i in list_title:
        if i == '%':
            new_list.append('\'')
        else:
            new_list.append(i)
    dec = f.decrypt("".join(new_list))
    return render_template('index.html', name=dec.decode())

app.run(debug=True, port=5003)