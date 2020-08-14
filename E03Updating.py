from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///d:/NewDatabase.db3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Example(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    data = db.Column("data", db.Unicode)

    def __init__(self, id, data):
        self.id = id
        self.data = data

if __name__ == "__main__":
    one = Example.query.filter_by(id=1).first()
    one.data = "Updated!"
    db.session.commit()
