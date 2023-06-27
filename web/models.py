from web import db
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False,unique=True)
    password  = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    stories = db.relationship('Userstory')
    appointments = db.relationship('Appointment')

class Userstory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())
    scheduled_time = db.Column(db.DateTime, nullable=False)
    approved = db.Column(db.Boolean, nullable=False,default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#class Reminder() to do list send reminders of appoitment



