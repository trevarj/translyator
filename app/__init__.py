__author__ = 'trevor'
from flask import Flask

translyator = Flask(__name__)
translyator.config.from_object('config')

from app import views