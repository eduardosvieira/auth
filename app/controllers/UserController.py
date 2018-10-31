from flask import render_template, request, jsonify, redirect, session

from app import app

app.config["SECRET_KEY"] = "sjakjs45454s@#4s8as9s997"

from app.models.User import User
from app.models.Criptografia import Criptografia

#verify login user
@app.route("/auth/login/", methods=["POST"])
def login():
  email = request.form.get("email")
  password = request.form.get("password")

  user = User()

  result = user.login(email=email, password=password)

  if result:
    message = {
      "name": result["name"],
      "email": email,
      "message": "OK",
      "code": 200,
      "modules": result["modules"]
    }

    token = Criptografia().encode(message)

    session["token"] = token

    return redirect("/abtms/modules/")
  else:
    message = {
      "name": "",
      "email": "",
      "message": "NOT FOUND",
      "code": 404
    }

    token = Criptografia().encode(message)

    return redirect("/abtms/login/")

@app.route("/auth/signup/", methods=["GET"])
def redirect_signup():
  return render_template("signup.html")


@app.route("/auth/signup/", methods=["POST"])
def signup():
  name = request.form.get("name")
  email = request.form.get("email")
  password = request.form.get("password")

  user = User(name=name, email=email, password=password)

  result = user.signup(user=user)

  return render_template("login.html", warning="O usuário foi cadastrado com sucesso!")


def check(email="", system=""):
    user = User()

    result = user.check_permissions(email=email, system=system)

    return result
