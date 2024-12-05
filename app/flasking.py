from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

from place import Place
from api_calls import *

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    list = text_search_from(36.663024, -121.769599, 10, 5000)
    return render_template('home.html', places = list)