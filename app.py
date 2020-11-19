from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index(name='Name'):
    title = request.args.get('title', 'default')
    return render_template('index.html', name=name, title=title)

@app.route('/catalog', methods=['GET', 'POST'])
def catalog_post():
    if request.method == 'GET':
        param = request.args['param']
    if request.method == 'POST':
        param = request.form['param']
    return f'\nParam: {param}'
#
# @app.route('/catalog')
# def catalog():
#     return "catalog!!!"

app.run(debug=True, port=5005)