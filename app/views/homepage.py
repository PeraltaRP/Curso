from app import app
@app.route('/') #decorator
def homePage():
    return "Hello, World!!!!"
