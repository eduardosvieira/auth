from flask import Flask, render_template, session
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://eduardo:senha@200.137.131.118/cfdb")

db = client.cfdb

from app.controllers import UserController
from app.models.Criptografia import Criptografia

#route to modules page
@app.route("/abtms/modules/")
def front():
    result = Criptografia().decode(session["token"])
    print(result)
    return render_template("modules.html", modules=result["modules"])

#route to login page
@app.route("/abtms/login/", methods=["GET"])
def redirect_login():
  return render_template("login.html")


@app.route("/abtms/")
def index():
    return render_template("student.html")
