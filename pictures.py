import flask, flask.views
import os
import utils

class Pictures(flask.views.MethodView):
	def get(self):
		folders = os.listdir('static/pictures/')
		return flask.render_template("pictures.html", folders = folders)
		
		
		#{{ picture }}
		#src = "/static/pictures/" + {{ picture }}
		#       	<li><a href="javascript:void(0);">{{picture}}</a></li>
		#	    				document.getElementById("pictures").appendChild(img);
