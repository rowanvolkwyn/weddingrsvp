from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#Specifying the location of the local SQL Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///weddinglist.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)