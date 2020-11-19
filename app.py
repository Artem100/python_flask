from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name='Name'):
    title = request.args.get('title', 'default')
    return render_template('index.html', name=name, title=title)

@app.route('/catalog', methods=['POST'])
def catalog_post():
    param = request.form['param']
    return param
#
# @app.route('/catalog')
# def catalog():
#     return "catalog!!!"

app.run(debug=True, port=5005)