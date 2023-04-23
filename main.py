from bottle import route, run

@route('/')
def default():
    return "This is the default web page of bc-mundo."

@route('/hello')
def hello():
    return "Hello World."

@route('/hello/<nom>')
def hello(nom):
    return "Hello World " + nom

run(host='localhost', port=8080, debug=True)