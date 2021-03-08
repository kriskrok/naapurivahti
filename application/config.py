from os import environ, path
from dotenv import load_dotenv

rootdir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(rootdir, '.env'))

class Config:
	"""Base config."""
	SECRET_KEY = environ.get('SESSION_KEY')
	#SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
	STATIC_FOLDER = 'static'
	TEMPLATES_FOLDER = 'templates'

class HerokuConfig(Config):	
	SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
	SQLALCHEMY_ECHO = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class LocalProdConfig(Config):
	"""Prod is ran on Gunicorn, but can't hurt to roleplay production
	circumstances every now and then. Do note, this uses DEV database URI"""
	FLASK_ENV = 'production'
	DEBUG = False
	TESTING = False
	SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URI')


class DevConfig(Config):
	FLASK_ENV = 'development'
	DEBUG = True
	TESTING = True			#Propagates exceptions
	SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URI')
	SQLALCHEMY_ECHO = True
	SQLALCHEMY_TRACK_MODIFICATIONS = True
