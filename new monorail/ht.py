from distutils.log import debug
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask_bootstrap import Bootstrap
import sys
app=Flask(__name__,template_folder='templates')


# Flask-Bootstrap requires this line
Bootstrap(app)

# the name of the database; add path if necessary
conn="mysql+pymysql://{0}:@{1}/{2}".format('root','localhost','monorail')


app.config['SECRET_KEY'] = 'SuperSecretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = conn
# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)

# each table in the database needs a class to be created for it
# db.Model is required - don't change it
# identify all columns by name and data type
class Train(db.Model):
    __tablename__ = 'trains'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    status = db.Column(db.String)
    departure_time = db.Column(db.String)
    expected_at = db.Column(db.String)
    average_speed = db.Column(db.Integer)
    position = db.Column(db.String)
    current_sector = db.Column(db.String)
    route = db.Column(db.String)
    delay_time=db.Column(db.String)
class maintenance(db.Model):
    __tablename__ = 'maintenance'
    TR_ID = db.Column(db.Integer)
    schedule_ID  = db.Column(db.Integer, primary_key=True)
    maintenance_start_date = db.Column(db.String)
    maintenance_end_date = db.Column(db.String)
    new_TR_ID= db.Column(db.Integer)

@app.route('/')
def index():
    try:
        return render_template('home.html')
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text
@app.route('/report')
def trainreport():
    try:
        trains = Train.query.order_by(Train.id).all()
        return render_template('TrainReport.html', trains=trains)
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text
@app.route('/maintenance')
def maintenancerep():
    try:
        maintenances = maintenance.query.order_by(maintenance.schedule_ID).all()
        return render_template('maintenance.html', maintenances=maintenances)
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text
if __name__ == '__main__':
    app.run(debug=True)