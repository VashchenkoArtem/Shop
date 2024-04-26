from shop.settings import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(255))
    password = db.Column(db.String(20))
     
    def __repr__(self) -> str:
        return f"Користувач - {self.name}"
