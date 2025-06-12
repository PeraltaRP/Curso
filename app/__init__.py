from flask import Flask

app = Flask(__name__)


from app.views.homepage import homePage
