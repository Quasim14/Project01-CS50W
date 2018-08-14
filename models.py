from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model) :
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key =True)
    isbn = db.Column(db.String(10))
    title = db.Column(db.String(255))
    author = db.Column(db.String(255))
    year = db.Column(db.Integer)


class User(db.Model) :
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))



