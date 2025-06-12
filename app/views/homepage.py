from app import app
from flask import render_template

@app.route('/') #decorator
def homePage():
    return  render_template('index.html')
