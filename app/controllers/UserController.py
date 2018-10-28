from flask import render_template, request, jsonify

from app import app

from app.models.User import User

@app.route("/auth/login/", methods=["GET"])
def redirect_login():
  return render_template("login.html")


@app.route("/auth/login/<system>", methods=["POST"])
def login(system):
  email = request.form.get("email")
  password = request.form.get("password")

  user = User()

  result = user.login(email=email, password=password)

  if result:
    return redirect("auth/modules/")
  else:
    message = {
      "name": "",
      "email": "",
      "message": "NOT FOUND",
      "code": 404
    }

  return jsonify(message)


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

    if check(email=result["email"], system=system):
      message = {
        "name": result["name"],
        "email": result["email"],
        "message": "OK",
        "code": 200
      }
    else:
      message = {
        "name": result["name"],
        "email": result["email"],
        "message": "FORBIDDEN",
        "code": 403
      }
  user = User()

  result = user.check_permissions(email=email, system=system)

  return result
