import datetime 

from flask import render_template


from . import app




@app.route('/')
def hello():
    return 'Hello World'

@app.route('/time') #this line makes this a view(instead of just a fct) by creating a path
def get_time():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')

@app.route('/pretty')
def pretty():
    context = {'who': 'Flo'}
    return render_template('pretty.html', **context)

