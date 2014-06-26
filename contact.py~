import flask, flask.views
import smtplib
from email.mime.text import MIMEText

#sitetest97@gmail.com
username = 'textest22@gmail.com'
password = 'testext22'
toaddrs  = 'tannerco97@gmail.com'

class Contact(flask.views.MethodView):
    def get(self):
        return flask.render_template('contact.html')
    
    def post(self):
		required = ['email', 'message', 'name']
		for r in required:
			if r not in flask.request.form:
				flask.flash("Error: {0} is required.".format(r))
				return flask.redirect(flask.url_for('contact'))
			else:
				flask.flash('w')
		name = flask.request.form['name']		
		email = flask.request.form['email']
		message = flask.request.form['message'] 
		# The actual mail send
		msg = MIMEText("Email From: " + name + "\n" +message)
		msg['Subject'] = email
		msg['From'] = email
		msg['To'] = toaddrs
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls()
		server.login(username,password)
		server.sendmail(email, [toaddrs], msg.as_string())
		server.quit()
		return flask.redirect(flask.url_for('contact'))               
