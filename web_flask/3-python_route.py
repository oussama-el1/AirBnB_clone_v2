#!/usr/bin/python3
""""import flask"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """helo world"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnh():
    """disply hbnb in /hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """c is fun"""
    tmp = text.replace('_', ' ')
    return "C {}".format(tmp)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscoool(text='is cool'):
    """python is cool"""
    return "Python " + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
