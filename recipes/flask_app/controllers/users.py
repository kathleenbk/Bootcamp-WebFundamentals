from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask import render_template, session,flash,redirect, request
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template("index.html")


# Create new user
@app.route('/register', methods=['POST'])
def register():
    # Validate registration
    is_valid = User.validate(request.form)
    if not is_valid:
        return redirect('/')
    
    # If registration is valid, save
    new = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(new)
    if not id:
        flash("Email already in use")
        return redirect('/')
    session['user_id'] = id
    return redirect('/dashboard')


# User Login
@app.route('/login', methods=['POST'])
def login():
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)

# Check if user is in db and if password is correct
    if not user_in_db:
        flash("Incorrect Email/Password", "login")
        return redirect("/")

    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Incorrect Email/Password", "login")
        return redirect('/')

# Log user in
    session['user_id'] = user_in_db.id
    return redirect('/dashboard')

# User Page
@app.route('/dashboard')
def home():
    if 'user_id' in session:
        
        data={
            "id":session['user_id']
        }
        user=User.get_one(data)
        all_recipes=Recipe.get_all_recipes()
        return render_template("dashboard.html",  user=user, all_recipes=all_recipes)
    if not 'user_id' in session:
        return redirect('/')

# Logout, clears session
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')