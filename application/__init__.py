### Behold all that will be initialized upon startup
import os, logging, sys
from flask import Flask
from flask_login import LoginManager, login_manager
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv() #TODO:// Find out why this is required to be invoked

from flask_sqlalchemy import SQLAlchemy

if os.environ.get('HEROKU'):
    print('HEROKU enviroment variable found: ', os.environ.get('HEROKU'))

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URL')
    # Set SQLAlchemy to print all SQL-queries
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = os.getenv('SESSION_KEY')
print('Todays session lottery is won by:', os.environ.get('SESSION_KEY'))

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

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

# Login functionality
from application.auth.models import Account
#from os import urandom
#app.config["SECRET_KEY"] = urandom(32)
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'authenticate_login'
login_manager.login_message = 'Olokkee hyvä ja enstöiksenne kirjautukkee sissää'

@login_manager.user_loader
def load_user(user_id):
    return Account.query.get(user_id)


try:
    pass
#    db.create_all()
except:
    pass
db.create_all()