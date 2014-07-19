from __future__ import with_statement
from flask import Flask, request, session, redirect, url_for, abort, \
     render_template, flash
from sqlalchemy import create_engine, Column, Integer, String, desc, asc
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import flask, flask.views
import os
import functools
import utils
import time
from datetime import date

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
time_keeper = date(2011, 11, 11)

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

DATABASE = 'sqlite:////home/jesse/parts-1/events.db'

engine = create_engine(DATABASE, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Entry(Base):
    __tablename__ = 'events'
    name = Column(String())
    description = Column(String())
    location = Column(String())
    link = Column(String())
    edate = Column(String())
    time = Column(String())
    till = Column(Integer, primary_key=True)

    def __init__(self, name='Event', description = '', location = 'here', link = '', edate = '', time = '', till = 0):
        self.name = name
        self.description = description
        self.location = location
        self.link = link
        self.edate = edate
        self.time = time
        self.till = till

def init_db_events():
    Base.metadata.create_all(bind=engine)

@app.teardown_request
def teardown_request(exception):
    db_session.remove()   		
    
class Event(flask.views.MethodView):
    def get(self):
    	today = date.fromtimestamp(time.time())
    	today_count = abs(today - time_keeper)
    	return flask.render_template('events.html', entries=Entry.query.order_by(asc(Entry.till)).all(), today=today_count.days)

    @utils.login_required
    def post(self):	
    		today = date.fromtimestamp(time.time())
    		today_count = abs(today - time_keeper)
		time_event = date(int(request.form['year']), int(request.form['month']), int(request.form['day']))
		time_to_event = abs(time_event - time_keeper)
		e = Entry(request.form['name'], request.form['description'], request.form['location'], request.form['link'], 
		months[int(request.form['month']) - 1] + ' ' + request.form['day'] + ', ' + request.form['year'], request.form['time'], int(time_to_event.days))
		db_session.add(e)
		db_session.commit()
		return flask.render_template('events.html', entries=Entry.query.order_by(asc(Entry.till)).all(), today=today_count.days) 
