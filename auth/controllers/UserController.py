from flask import render_template, request, jsonify, redirect, session

from app import app

from app.models.User import User
from app.models.Encrypto import Encrypto

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
      "code": 200
    }

  else:
    message = {
      "name": "",
      "email": "",
      "message": "NOT FOUND",
      "code": 404
    }

  token = Encrypto().encode(message)

  return token

@app.route("/auth/signup/", methods=["POST"])
def signup():
  name = request.form.get("name")
  email = request.form.get("email")
  password = request.form.get("password")

  user = User(name=name, email=email, password=password)

  result = user.signup(user=user)

  if result:
    return "OK", 200
  else:
    return "Error", 404
