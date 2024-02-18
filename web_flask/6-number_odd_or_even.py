#!/usr/bin/python3
""""import flask"""
from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def usetemplate(n):
    """display html if a int is passed"""
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    if n % 2 == 0:
        status = 'even'
    else:
        status = 'odd'
    return render_template('6-number_odd_or_even.html', num=n, status=status)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
