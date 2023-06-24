from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import path
from flask_login import LoginManager
#databse environment variables
db = SQLAlchemy()
DB_NAME  = 'Mending_minds_db'
DB_USER = 'root'
USER_PWD = 'Ben101242!'
HOST = 'localhost'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'wertyuiobnm'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{DB_USER}:{USER_PWD}@{HOST}/{DB_NAME}'
    db.init_app(app)
    
    
    #Register bluebrint
    from web.views import views
    from web.auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # define classes before db creation
    from web.models import User,Userstory,Appointment
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.Login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

#def create_db(app):
 #   if not path.exists('web/'+ DB_NAME):
  #      db.create_all(app=app)
   #     print('db created')

 