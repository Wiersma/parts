import flask, flask.views
import os
import utils

class Videos(flask.views.MethodView):
	def get(self):
		folders = os.listdir('static/videos/')
		return flask.render_template("videos.html", folders = folders)
