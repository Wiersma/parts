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

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

DATABASE = 'sqlite:////home/tanner/projects/flask/parts/members.db'

engine = create_engine(DATABASE, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Entry(Base):
    __tablename__ = 'members'
    id = Column(Integer, primary_key=True)
    picture = Column(String())
    name = Column(String())
    bio = Column(String())
    directory = Column(String())

    def __init__(self, picture='doe.jpg', name='John Doe', bio = '', directory = ''):
        self.picture = picture
        self.name = name
        self.bio = bio
        self.directory = directory

def init_db_members():
    Base.metadata.create_all(bind=engine)

@app.teardown_request
def teardown_request(exception):
    db_session.remove()   		
    
class Members(flask.views.MethodView):
    def get(self):
    	path = request.args.get('directory')
    	return flask.render_template('members.html', entries=Entry.query.order_by(desc(Entry.id)).all(), directory=path)

    @utils.login_required
    def post(self):
    		path = request.args.get('directory')
		e = Entry(request.form['photo'], request.form['name'], request.form['bio'], request.args.get('directory'))
		db_session.add(e)
		db_session.commit()
		return flask.render_template('members.html', entries=Entry.query.order_by(desc(Entry.id)).all(), directory=path)  
