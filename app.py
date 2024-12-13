from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cmt.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class cmt(db.Model):
    email=db.Column(db.String(50),primary_key=True)
    password=db.Column(db.String(16),nullable=False)
    name=db.Column(db.String(20),nullable=False)
    org=db.Column(db.String(20),nullable=False)
    phone=db.Column(db.Integer,nullable=False)
    doc=db.Column(db.DateTime,default=datetime.utcnow)
@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/products")
def events():
    return "This is a products page!</p>"

if __name__=="__main__":
    app.run(debug=True)