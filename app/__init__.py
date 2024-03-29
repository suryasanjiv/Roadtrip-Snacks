# app/__init__.py

from flask import Flask

#init app
app = Flask(__name__, instance_relative_config=True)

from app import views 

app.config.from_object('config')