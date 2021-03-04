### Behold all that will be initialized upon startup

import os, logging, sys
from flask import Flask
from flask_login import LoginManager, login_manager
from dotenv import load_dotenv

from flask_sqlalchemy import SQLAlchemy

load_dotenv() 

app = Flask(__name__)

if os.environ.get('HEROKU'):
    print('HEROKU enviroment variable found: ', os.environ.get('HEROKU'))
    app.config.from_object('application.config.HerokuConfig')
else:
    print('Could not find HEROKU enviroment variable')
    app.config.from_object('application.config.DevConfig')
    print('Todays session lottery is won by:', os.getenv('SESSION_KEY')[:5], '... \ncongratulations to all the winners!')


if (True): #TODO:// Conjure a nifty debug variable 
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
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'authenticate_login'
login_manager.login_message = 'Olokkee hyvä ja enstöiksenne kirjautukkee sissää'

@login_manager.user_loader
def load_user(user_id):
    return Account.query.get(user_id)


try:
    db.create_all()
except:
    pass
