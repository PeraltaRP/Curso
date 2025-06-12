from flask import Flask

app = Flask(__name__)
# Importing views
from app.views.views import homePage