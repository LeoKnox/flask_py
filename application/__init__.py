from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
import pymongo

app = Flask(__name__)
app.config.from_object(Config)

db = MongoEngine()
db.init_app(app)

myclient = pymongo.MongoClient('mongodb://localhost:27017')
mydb = myclient['Flask_App']
mycol = mydb["room"]

from application import routes