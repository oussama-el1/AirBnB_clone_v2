#!/usr/bin/python3
"""Lists of states"""
from flask import Flask, render_template
from models import *
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def fetchdata():
    """display list of state"""
    states = list(storage.all(State).values())
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', data=sorted_states)


@app.teardown_appcontext()
def removesession(exception):
    """remove session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
