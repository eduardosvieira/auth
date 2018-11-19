from app.models.DatabaseFactory import DatabaseFactory

class User():
  def __init__(self, code=0, name="", email="", password=""):
    self.code = code
    self.name = name
    self.email = email
    self.password = password
    self.connection = DatabaseFactory().getConnection()


  def login(self, email="", password=""):
    try:
      with self.connection.cursor() as cursor:
        sql = "SELECT `id`, `name` FROM `users` WHERE `email`=%s AND password=%s"
        cursor.execute(sql, (email, password))
        result = cursor.fetchone()

        if result:
          return result
        else:
          return None
    finally:
      self.connection.close()


  def signup(self, user=None):
    try:
      with self.connection.cursor() as cursor:
        sql = "INSERT INTO `users` (`name`, `email`, `password`) VALUES (%s, %s, %s)"
        cursor.execute(sql, (user.name, user.email, user.password))
        self.connection.commit()
    
        return True
      
    finally:
      self.connection.close()

  def check_permissions(self, user="", module=""):
    try:
      with self.connection.cursor() as cursor:
        sql = "SELECT * FROM access WHERE user=%s AND module=%s"
        cursor.execute(sql, (user, module))
        result = cursor.fetchone()

        if result:
          return True
        else:
          return False
    finally:
      self.connection.close()
