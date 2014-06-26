from __future__ import with_statement
from flask import Flask, request, session, redirect, url_for, abort, \
     render_template, flash
from sqlalchemy import create_engine, Column, Integer, String, desc
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import flask, flask.views
import os
import functools
import utils
from time import gmtime, strftime

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

DATABASE = 'sqlite:////home/tanner/projects/flask/parts/newsfeed.db'

engine = create_engine(DATABASE, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(String())
    text = Column(String())
    time = Column(String())

    def __init__(self, title='Untitled', text='', time = ''):
        self.title = title
        self.text = text
        self.time = strftime("%Y-%m-%d %H:%M:%S", gmtime())

def init_db():
    Base.metadata.create_all(bind=engine)

@app.teardown_request
def teardown_request(exception):
    db_session.remove()   		
    
class Feed(flask.views.MethodView):
    def get(self):
    	return flask.render_template('show_entries.html', entries=Entry.query.order_by(desc(Entry.id)).all())

    @utils.login_required
    def post(self):
		e = Entry(request.form['title'], request.form['text'])
		db_session.add(e)
		db_session.commit()
		return flask.render_template('show_entries.html', entries=Entry.query.order_by(desc(Entry.id)).all())  
		
    
    
    
    
    
    
    
