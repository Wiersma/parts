import flask
import settings

# Views
from login import Login
from remote import Remote
from main import Main 
from newsfeed import Feed, init_db
from pictures import Pictures
from display_pictures import Display
from videos import Videos
from display_videos import vidDisplay
from contact import Contact
from donate import Sponsors
from members import Members, init_db_members
from home import Home

app = flask.Flask(__name__)
app.secret_key = settings.secret_key

# Routes
app.add_url_rule('/',
                 view_func=Home.as_view('home'),
                 methods=["GET", "POST"])
app.add_url_rule('/<page>/',
                 view_func=Main.as_view('page'),
                 methods=["GET"])
app.add_url_rule('/login/',
                 view_func=Login.as_view('login'),
                 methods=["GET", "POST"])
app.add_url_rule('/remote/',
                 view_func=Remote.as_view('remote'),
                 methods=["GET", "POST"])
app.add_url_rule('/add/',
                 view_func=Feed.as_view('add_entry'),
                 methods=["GET", "POST"])
app.add_url_rule('/pictures/',
                 view_func=Pictures.as_view('pictures'),
                 methods=["GET", "POST"])
app.add_url_rule('/display_pictures/',
                 view_func=Display.as_view('display_pictures'),
                 methods=["GET", "POST"])
app.add_url_rule('/videos/',
                 view_func=Videos.as_view('videos'),
                 methods=["GET", "POST"])
app.add_url_rule('/display_videos/',
                 view_func=vidDisplay.as_view('display_videos'),
                 methods=["GET", "POST"])                 
app.add_url_rule('/contact/',
                 view_func=Contact.as_view('contact'),
                 methods=["GET", "POST"]) 
app.add_url_rule('/donate/',
                 view_func=Sponsors.as_view('support'),
                 methods=["GET"])
app.add_url_rule('/members/',
                 view_func=Members.as_view('members'),
                 methods=["GET", "POST"])                                    
                                 
@app.errorhandler(404)
def page_not_found(error):
    return flask.render_template('404.html'), 404

app.debug = True
if __name__ == "__main__":
	init_db()
	init_db_members()
	app.run()
