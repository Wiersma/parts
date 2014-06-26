import flask, flask.views
from flask import request
import os
import utils

class Sponsors(flask.views.MethodView):
	def get(self):
		pictures = os.listdir('static/sponsors/')
		return flask.render_template("support.html", pictures = pictures)
