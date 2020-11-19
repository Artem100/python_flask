from flask import Flask, render_template, request, make_response, session

app = Flask(__name__)
app.secret_key = b'093rj3984fjrfj'

@app.route('/')
def index():
    # Работа с куками
    visited = 0
    if request.cookies.get('visited'):
        visited = int(request.cookies.get('visited'))
    resp = make_response(render_template('index.html', visited=visited))
    resp.set_cookie('visited', str(visited+1))
    return resp

@app.route('/session')
def session_page():
    var_session = 0
    if session.get('var_session'):
        var_session = int(session.get('var_session'))
    else:
        session['var_session'] = 0

    resp = make_response(render_template('index.html', var_session=var_session))
    session['var_session'] += 1
    return resp

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

app.run(debug=True, port=5007)