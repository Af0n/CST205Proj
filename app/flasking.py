from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm 
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

from place import Place
from api_calls import *

# cmd to run to start
# flask --app flasking --debug run

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap5(app)

place_list = []
message = ""

class searchInfo(FlaskForm):
    address = StringField(
        'Address', 
        validators=[DataRequired()]
    )
    range = IntegerField(
        'Range(in meters)', 
        validators=[DataRequired()]
    )

@app.route('/', methods=('GET', 'POST'))
def index():
    global message
    message = ""
    if(len(place_list) < 1):
        return redirect('/search')
    return render_template('index.html', locations = place_list)

@app.route('/search')
def search():
        sI = searchInfo()
        return render_template('search.html', form = sI, msg = message)

@app.route('/postsearch', methods=('GET', 'POST'))
def post_search():
    sI = searchInfo()
    if sI.validate_on_submit():
        print("=====" + str(sI.address) + " " + str(sI.range) + "=====")
        global place_list
        place_list = converter(sI.address.data, sI.range.data)
        if(len(place_list) > 0):
            return redirect('/')
        global message
        message = "Address too broad. Please enter more information such as a city or ZIP code."
        return redirect('/search')


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
