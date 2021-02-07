### Behold all that will be initialized upon startup
from os import getenv
from dotenv import load_dotenv
from flask import Flask
app = Flask(__name__)

load_dotenv() #TODO:// Find out why this is required to be invoked

from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = getenv('DATABASE_URL')

# Set SQLAlchemy to print all SQL-queries
app.config["SQLALCHEMY_ECHO"] = True

# db object for all our ORM needs
db = SQLAlchemy(app)

# Import functionality
from application import views

from application.auth import models
from application.auth import views

from application.report import models
from application.report import views

from application.shift import models
from application.shift import views

try:
    pass
#    db.create_all()
except:
    pass
db.create_all()