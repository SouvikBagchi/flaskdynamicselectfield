#IMPORT FLASK
from flask import Flask, jsonify

#FOR BACKEND SQL DATABASE CONNECTION
from flask_sqlalchemy import SQLAlchemy 

#FOR ERROR LOGGING
from logging import FileHandler, WARNING

#FOR CSRF PROTECTION WHILE SUBMITTING FORMS
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
# set the configuration
app.config.from_object('settings')

#create the db instance of SQLAlchemy
db = SQLAlchemy(app)


#ERROR LOGGIN
#LOGS ERROR TOO THE FILE CALLED - errorlog.txt
file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)
app.logger.addHandler(file_handler)

#SET SECRET KEY
app.secret_key = "some_strong_secret_key"

#IMPORT VIEWS WHICH IS THE CONTROLLER IN THE MVC
import views