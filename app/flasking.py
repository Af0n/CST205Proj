from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

from place import Place
from api_calls import *

# cmd to run to start
# flask --app flasking --debug run

app = Flask(__name__)
bootstrap = Bootstrap5(app)

place_list = []

@app.route('/')
def index():
    return render_template('index.html', locations = place_list)


@app.route('/detail/<int:index>')
def inspect(index):
    #Azrael, takes in t
    return render_template('placetest.html', places = [place_list[index]])

@app.route('/placetest')
def place_test():
    # temporary location latitude/longitude
    global place_list 
    place_list = converter("San Francisco Tenderloin", 5000)
    return render_template('placetest.html', places = place_list)
