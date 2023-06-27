#This the authentication bluebrint of our app
from flask import Blueprint, render_template, request, flash
from web.models import User, db
# redirect user 
from flask import redirect, url_for
#secure password
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def Login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        #query db for credentials
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('logged in', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.index'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash('user doesnt exist, please Sign up')
            return redirect(url_for('auth.SignUP'))

    return render_template('login.html', user=current_user)

@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def Logout():
    logout_user()
    return redirect(url_for('auth.index'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def SignUP():
    if request.method == 'POST':
        email =request.form.get('email')
        firstName = request.form.get('firstname')
        lastName = request.form.get('lastname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        #check if user dosent already exist
        user = User.query.filter_by(email=email).first()
        if user:
            flash('User already exists', category='error')
        elif len(email) < 2:
            flash('email too short', category='error')
        elif len(firstName) < 2:
            flash('name too short', category='error')
        elif len(password1) < 8:

            flash('password must be  8 characters', category='error')
        elif len(lastName) < 1:
            flash('Enter last name')

        elif password1 != password2:
            flash('paswords do not match', category='error')
        else:
            new_user = User(email=email, first_name=firstName, last_name=lastName, password=generate_password_hash(password1, method='MD5'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created', category='success')
            return redirect(url_for('auth.Login'))

    
    return render_template('sign-up.html', user=current_user)

