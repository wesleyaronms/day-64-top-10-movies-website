from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.String, unique=False, nullable=False)
    description = db.Column(db.String(250), unique=True, nullable=True)
    rating = db.Column(db.Float, unique=False, nullable=False)
    ranking = db.Column(db.Integer, unique=False, nullable=True)
    review = db.Column(db.String(250), unique=False, nullable=True)
    img_url = db.Column(db.String(500), unique=True, nullable=False)

    def __repr__(self):
        return f"Movie {self.title}"


# Para criar o banco de dados pela primeira vez; comando pode ser executado no console.
# db.create_all()
