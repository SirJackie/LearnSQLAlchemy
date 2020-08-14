from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///d:/NewDatabase.db3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Example(db.Model):
    __tablename__ = "Example"

    id = db.Column("id", db.Integer, primary_key=True)
    data = db.Column("data", db.Unicode)

    def __init__(self, id, data):
        self.id = id
        self.data = data

if __name__ == "__main__":
    new_ex = Example(1, "Hello World!")
    db.session.add(new_ex)
    db.session.commit()
