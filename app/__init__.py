from flask import Flask


app = Flask(__name__)  #first create app so that when we jump into views we have app to grab
app.config.from_object('config')

from . import views 
