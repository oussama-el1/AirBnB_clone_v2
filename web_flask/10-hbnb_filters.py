#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage


app = Flask(__name__)


@app.route('/hbnb_filters')
def filtter():
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    amintys = sorted(list(storage.all("Amenity").values()),
                     key=lambda x: x.name)
    return render_template('10-hbnb_filters.html', states=states,
                           amintys=amintys)


@app.teardown_appcontext
def close_db(exception):
    """remove the current sqlalchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
