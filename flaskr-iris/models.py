from .database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(1000), unique=True, nullable=False)
    password = db.Column(db.String(1000), nullable=False)
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    created = db.Column(db.Time, nullable=False, server_default=db.text('CURRENT_TIMESTAMP'))
    title = db.Column(db.String(1000), nullable=False)
    body = db.Column(db.String(1000000))
    
