from app import app
from flask import render_template


@app.route('/')
@app.route('/abhinav')
@app.route('/index')
def index():
    duser = {'username': 'Abhinav'}
    # return render_template('index.html',title='Home',user=duser)
    return render_template('index.html', user=duser)
