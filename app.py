from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "dialect://root:radhasoami@localhost:port/cmt"
db=SQLALCHEMY(app)
@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/products")
def events():
    return "This is a products page!</p>"

if __name__=="__main__":
    app.run(debug=True)