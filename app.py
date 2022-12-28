import flask
from flask import Flask
from flask_wp import FlaskWP
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_BINDS'] = {
    "wordpress" : "mysql://doadmin:@dbaas-db-5470089-do-user-13178331-0.b.db.ondigitalocean.com:25060/defaultdb"
}
db = SQLAlchemy(app)
fwp = FlaskWP(db, app)

@app.route("/")
def index():
    return flask.jsonify([{'user_email': usr.user_email} for usr in fwp.User.query.all()])

if __name__ == "__main__":
    app.run(debug=True)
