from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from place import Place
from api_calls import *

# cmd to run to start
# flask --app flasking --debug run

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap5(app)

place_list = []
place_list = text_search_from(36.663024, -121.769599, 10, 5000)

class searchInfo(FlaskForm):
    address = StringField(
        'Address', 
        validators=[DataRequired()]
    )
    range = StringField(
        'Range(in meters)', 
        validators=[DataRequired()]
    )

@app.route('/', methods=('GET', 'POST'))
def index():
    if(len(place_list) < 1):
        return redirect('/search')
    return render_template('index.html', locations = place_list)

@app.route('/search', methods=('GET', 'POST'))
def search():
        sI = searchInfo()
        if sI.validate_on_submit():
            print("=====" + str(sI.address) + " " + str(sI.range) + "=====")
            # converter(sI.address, sI.range)
            return redirect('/index')
        return render_template('search.html', form = sI)


@app.route('/detail/<int:index>')
def inspect(index):
    #Azrael, takes in t
    return render_template('placetest.html', places = [place_list[index]])

@app.route('/placetest')
def place_test():
    # temporary location latitude/longitude
    place_list = text_search_from(36.663024, -121.769599, 10, 5000)
    return render_template('placetest.html', places = place_list)
