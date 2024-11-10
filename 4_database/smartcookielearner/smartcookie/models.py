import sqlalchemy as sa
from werkzeug.security import generate_password_hash, check_password_hash
from smartcookie import db

class User(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64), 
                         index=True, unique=True)
    email = db.Column(db.String(120), 
                      index=True, unique=True)
    password_hash = db.Column(db.String(256))

    def __repr__(self) -> str:
        return f'<User {self.username}>'
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
