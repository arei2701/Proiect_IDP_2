from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request
import json as JSON
from sqlalchemy.ext.declarative import DeclarativeMeta
from copy import copy, deepcopy
import random
import string

app =  Flask(__name__)
addr = "db"
#addr = "127.0.0.1"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:arei2701@' + addr + ':3306/my_new_database'
#app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class AlchemyEncoder(JSON.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    JSON.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields
        return JSON.JSONEncoder.default(self, obj)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/get_restos')
def get_restos():
    return JSON.dumps(db.session.query(Restos).all(), cls=AlchemyEncoder)


class Restos(db.Model):
    __tablename__ = 'Restos'
    id = db.Column(db.Integer, primary_key=True)
    rname = db.Column(db.String(60))
#    ora_plecare = db.Column(db.Integer)
    
    def __init__(self, nume):
        self.rname = nume
        #self.id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    
class Tables(db.Model):
    __tablename__ = 'Tables'
    id = db.Column(db.Integer, primary_key=True)
    resto_id = db.Column(db.Integer)
    max_people = db.Column(db.Integer)
    
    def __init__(self, resto_id, max_people):
        self.max_people = max_people
        #self.id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        self.resto_id = resto_id

class Bookings(db.Model):
    __tablename__ = 'Bookings'
    id = db.Column(db.Integer, primary_key = True)
    id_resto = db.Column(db.Integer)
    id_table = db.Column(db.Integer)
    client_name = db.Column(db.String(60))
    client_id = db.Column(db.String(60))
    bdate = db.Column(db.String(60))
    btime = db.Column(db.String(60))

#    ora_plecare = db.Column(db.Integer)
    
    def __init__(self, resto, table, name, cl_id, date, time):
        self.name = nume
        #self.id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        self.id_resto = resto
        self.id_table = table
        self.client_id = cl_id
        self.client_name = name
        self.bdate = date
        self.btime = time



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002, threaded=False)
