from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

from place import Place
from api_calls import *

# cmd to run to start
# flask --app flasking --debug run

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/placetest')
def place_test():
    # temporary location latitude/longitude
    list = text_search_from(36.663024, -121.769599, 10, 5000)
    return render_template('placetest.html', places = list)