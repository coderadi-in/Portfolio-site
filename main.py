'''coderadi &bull; Main file of the Project.'''

# ? IMPORTING LIBRARIES
from flask import Flask, render_template
from plugins import *
from routers import *

# ! LOADING VIRTUAL ENVIRONMENT
# ! [DEVELOPMENT ONLY]
from dotenv import load_dotenv
load_dotenv('.venv/vars.env')

# ! BUILDING SERVER
server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
server.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# ! BINDING PLUGINS & ROUTERS
bind_plugins(server)
bind_routers(server)

# ! INITIALIZING DATABASE
if (__name__ == '__main__'):
    with server.app_context():
        db.create_all()

# | ERROR HANDLING [START]

# & 404
@server.error_handler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

# & 500
@server.error_handler(500)
def internal_server_error(error):
    return render_template('errors/500.html'), 500

# | ERROR HANDLING [END]