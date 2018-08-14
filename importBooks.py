import csv
import os

from flask import Flask, render_template, request
from models import *


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:12345@localhost/project01'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():

    fbooks = open("books.csv")
    reader = csv.reader(fbooks)

    for isbn, title, author, year in reader :
        book = Book(isbn = isbn, title=title, author =author, year=year)
        db.session.add(book)
        print(f"Ajout du livre isbn : {isbn} , titre : {title}, auteur : {author}, année : {year}")

    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        main()