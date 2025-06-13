from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#variavel de banco de dados
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Importing views
from app.views.views import homePage

#criar arquivo models.py
from app.models.models import Contato

