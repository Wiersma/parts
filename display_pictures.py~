import flask, flask.views
from flask import request
import os
import utils

class Display(flask.views.MethodView):
	def get(self):
		folder = request.args.get('folder')
		images = os.listdir('static/pictures/' + folder)
		return flask.render_template("display_pictures.html", images = images, folder = folder)

		
		
		
		
		
		
		
		

