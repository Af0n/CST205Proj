from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

from place import Place
from api_calls import *

# cmd to run to start
# flask --app flasking --debug run

app = Flask(__name__)
bootstrap = Bootstrap5(app)

#Azrael To-Do get a function that calls thez
places = text_search_from(36.663024, -121.769599, 10, 5000)

@app.route('/')
def index():
    return render_template('index.html', locations = places)


@app.route('/detail/<int:index>')
def inspect(index):
    #Azrael, takes in t
    return render_template('placetest.html', places = [places[index]])

@app.route('/placetest')
def place_test():
    # temporary location latitude/longitude
    return render_template('placetest.html', places = places)