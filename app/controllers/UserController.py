from flask import render_template, request, jsonify

from app import app

from app.models.User import User
from app.models.Criptografia import Criptografia

@app.route("/auth/login/<module>/", methods=["GET"])
def redirect_login(module):
  return render_template("login.html", module=module)


@app.route("/auth/login/<system>", methods=["POST"])
def login(system):
  email = request.form.get("email")
  password = request.form.get("password")

  user = User()

  result = user.login(email=email, password=password)

  if result:
    if check(email=email, system=system):
      message = {
        "name": result["name"],
        "email": email,
        "message": "OK",
        "code": 200
      }
    else:
      message = {
        "name": result["name"],
        "email": email,
        "message": "FORBIDDEN",
        "code": 403
      }
  else:
    message = {
      "name": "",
      "email": "",
      "message": "NOT FOUND",
      "code": 404
    }

  cipher = Criptografia().encode(message)

  print(message)

  return cipher

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
