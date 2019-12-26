import os.path
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'cfa.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = '4NBn148Y4VkzFnN6o8Gk'