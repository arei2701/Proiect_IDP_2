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

@app.route('/remove_flight')
def remove_flight():
    keys = list(request.args.keys())
    if "id" not in keys:
        return ("N-am")
    id0 = request.args.get("id")
    print(id0)
    ac = db.session.query(Zbor).filter_by(id = id0).delete()
    db.session.commit()
    return "200"



@app.route('/add_flights')
def add_flights():
    keys = list(request.args.keys())
    print(list(keys))
    if "sursa" not in keys:
        return ("Da, unde plec bo$$?")
    sursa = request.args.get('sursa')

    if "destinatie" not in keys:
        return ("Da unde ziceai ca merg?")
    destinatie = request.args.get('destinatie')

    if "ora_plecare" not in keys:
        return ("Are we there yet? Are we there yet?")
    ora_plecare = int(request.args.get('ora_plecare'))

    if "zi_plecare" not in keys:
        return ("Intr-o zi cu soare")
    zi_plecare = int(request.args.get('zi_plecare'))

    if "durata" not in keys:
        return ("vreo 10 minute intr-o zi buna")
    durata = int(request.args.get('durata'))

    if "nr_locuri" not in keys:
        return ("Sa fie")
    nr_locuri = int(request.args.get('nr_locuri'))
   
    if not(ora_plecare >= 0 and ora_plecare <= 23):
        return ("Ora plecare nu ok")
    if not(ora_plecare >= 0 and ora_plecare <= 23):
        return ("Zi plecare nu ok")
    
    db.session.add(Zbor(sursa, destinatie, ora_plecare, zi_plecare, durata, nr_locuri))
    db.session.commit()
    return ("Flight added")

@app.route('/book_flight')
def book_flight():
    keys = list(request.args.keys())
    
    if "id" not in keys:
        return ("400", "Zi un numar, orice numar")
    ac = request.args.get('id')
    dc = Zbor.query.filter_by(id = ac).first()
    dc.rezervari += 1
    db.session.commit()
    return "Flight booked"

@app.route('/buy_ticket')
def buy_ticket():
    keys = list(request.args.keys())
    
    if "id" not in keys:
        return ("400", "Zi un numar, orice numar")
    ac = request.args.get('id')
    dc = Zbor.query.filter_by(id = ac).first()
    dc.bilete_vandute += 1
    db.session.commit()
    return "Ticket bought"


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
