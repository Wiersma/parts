import flask, flask.views
from flask import request
import os
import utils

class vidDisplay(flask.views.MethodView):
	def get(self):
		folder = request.args.get('folder')
		videos = os.listdir('static/videos/' + folder)
		return flask.render_template("display_videos.html", videos = videos, folder = folder)
