from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://eduardo:senha@200.137.131.118/cfdb")

db = client.cfdb

from app.controllers import UserController

@app.route("/auth/")
def front():
    return render_template("index.html")
