from flask import Flask, render_template

from models.state import State 
from models import storage, storage_t

app = Flask(__name__)

states = []
if storage_t == 'db':
    states = list(storage.all(State))
    
else:
    pass

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ cities for state """
    states = []
    if storage_t == 'db':
        states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    else:
        pass
    return render_template('8-cities_by_states.html', states=states, engine=storage_t)

@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)