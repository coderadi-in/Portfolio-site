'''coderadi &bull; Plugins file of the Project.'''

# ? IMPORTING LIBRARIES
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from twilio.rest import Client
import os

# ! INITIALIZING PLUGINS
db = SQLAlchemy()
migrator = Migrate()
client = Client(os.getenv("ACC_SID"), os.getenv("AUTH_TOKEN"))

# & DEFINING SOME CONSTANTS
REFERRALS = {
    "work": "I wanna work with you.",
    "connect": "I have a project to discuss with you.",
    "project": "I wanna build a project with you.",
    "error": "I've to report an error in your site."
}

# * FUNCTION TO BIND PLUGINS TO THE SERVER
def bind_plugins(server):
    db.init_app(server)
    migrator.init_app(server, db)

# * FUNCTION TO SEND WHATSAPP NOTIFICATIONS
def notify(body: str):
    client.messages.create(
        body=body,
        from_=f"whatsapp:{os.getenv('FROM_NUMBER')}",
        to=f"whatsapp:{os.getenv('TO_NUMBER')}",
    )

# | CONTACT DATABASE MODEL
class Contact(db.Model):
    '''Stores the info of user who had filled the contact form.'''

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100))
    message = db.Column(db.Text, nullable=False)

# | PROJECTS DATABASE MODEL
class Project(db.Model):
    '''Stores the info of projects.'''

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cover = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.TEXT, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False)
    achievements = db.Column(db.JSON, nullable=False)
    github = db.Column(db.String(100))
    accent = db.Column(db.String(20), nullable=False)
    tech_stack = db.Column(db.JSON, nullable=False)
    external = db.Column(db.Boolean, default=False)
    url = db.Column(db.String(100))

# | OFFERS DATABASE MODEL
class Offer(db.Model):
    '''Stores the info of offers.'''

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.TEXT, nullable=False)
    icon = db.Column(db.String(100), nullable=False)
    tags = db.Column(db.JSON, nullable=False)