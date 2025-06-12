from app import app
from flask import render_template
from flask import url_for

@app.route('/') #decorator
def homePage():
    usuario = 'Gustavo'
    return  render_template('index.html', usuario=usuario)


@app.route('/nova')
def nova():
    return ('ola mundo')