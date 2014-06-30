import flask, flask.views
import os
import utils

class Home(flask.views.MethodView):
    def get(self):
    	images = os.listdir('static/slider')
        return flask.render_template('home.html',images = images)
    
    def post(self):
    	pass
