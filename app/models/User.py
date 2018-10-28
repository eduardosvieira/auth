from app import db

class User():
  def __init__(self, code=0, name="", email="", password=""):
    self.code = code
    self.name = name
    self.email = email
    self.password = password

  
  def login(self, email="", password=""):
    u = db.users.find_one({
      "email": email,
      "password": password
    })

    if u:
      return u
    else:
      return None


  def signup(self, user=None):
    db.users.insert({
      "name": user.name,
      "email": user.email,
      "password": user.password, 
      "system_access": ["portal"]
    })

    return True

  
  def check_permissions(self, email="", system=""):
    u = db.users.find_one({"email": email, "system_access": system})

    if u:
      return True
    else:
      return False
