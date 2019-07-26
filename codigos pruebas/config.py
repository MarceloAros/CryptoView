import os

class Config(object):
	"""docstring for Config"""

class DevelopmentConfig(Config):
	"""docstring for DevelopmentConfig"""
	DEBUG = True
	SQLALCHEMY_DATABASE_URI= 'mysql://root:Cryptoview@localhost/flask'
		


