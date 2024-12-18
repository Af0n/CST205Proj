#Title The First Step
#Course 205 Multimedia Programming
#Project Members Andrew, Azrael, Zaheem
#General Credit
# Azrael made Index, Search, and small amounts of Flasking
# Andrew made placetest, api_calls, most of Flasking, and place.py, additionally they were extremely helpful in actually pulling everything together by being the one to merge everything.
# Zaheem, did style edits of index, search, and placetest
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

#The form for the search bar that takes in the Address, and Range so that it can be used to get the places. Made by Azrael
class searchInfo(FlaskForm):
    address = StringField(
        'Address', 
        validators=[DataRequired()]
    )
    range = IntegerField(
        'Range(in meters)', 
        validators=[DataRequired()]
    )

#Uses the global place_list to make a list of buttons that take you to a details page, made by Azrael
@app.route('/', methods=('GET', 'POST'))
def index():
    global message
    message = ""
    if(len(place_list) < 1):
        return redirect('/search')
    return render_template('index.html', locations = place_list)

#Passes a form to the template, which is then converted into useful data in order to create a useful list of places, made by Azrael, stylized by Zaheem.
@app.route('/search')
def search():
        sI = searchInfo()
        return render_template('search.html', form = sI, msg = message)

#takes in the data from search and applies it to the global place_list, made by Andrew
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

#Takes the place given to it by index.html and uses it to display important information. Route made by Azrael, Andrew made page.
@app.route('/detail/<int:index>')
def inspect(index):
    return render_template('placetest.html', places = [place_list[index]])

#Old code made by Andrew, for testing out the details page without a search page
@app.route('/placetest')
def place_test():
    # temporary location latitude/longitude
    global place_list 
    place_list = converter("San Francisco Tenderloin", 5000)
    return render_template('placetest.html', places = place_list)
