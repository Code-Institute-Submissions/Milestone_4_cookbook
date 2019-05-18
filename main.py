# Importing

import os, env
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from forms import LoginForm, RegistrationForm
from pprint import pprint


app = Flask(__name__)

app.config["MONGO_DBNAME"] = "cookbook"
app.config["MONGO_URI"] = os.environ.get('MONGO_URI', 'monogodb://localhost')
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')

mongo = PyMongo(app)

# Routing

@app.route('/recipe<recipe_id>')
def recipe(recipe_id):
    the_recipe =  mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    pprint(the_recipe)
    return render_template('recipe.html', recipe=the_recipe)

# Routing - Register - GET and POST method

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Function for handling the registration of users"""
    if session.get('logged_in'):
        if session['logged_in'] is True:
            return redirect(url_for('index'))

    form = RegistrationForm()

    if form.validate_on_submit():

        user = mongo.db.user
        dup_user = user.find_one({'name' : request.form['username'].title()})

        if dup_user is None:
            user.insert_one({'name' : request.form['username'].title()})
            session['username'] = request.form['username']
            session['logged_in'] = True
            return redirect(url_for('index'))

        flash('Sorry, username already taken. Please try another.')
        return redirect(url_for('register'))

    return render_template('register.html', form=form, title="Register")

# Routing - Login

@app.route('/login', methods=['GET', 'POST'])
def user_login():
    if session.get('logged_in'):
        if session['logged_in'] is True:
            return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = mongo.db.user
        logged_in_user = user.find_one({'name' : request.form['username'].title()})

        if logged_in_user is None:
            flash('Incorrect username, please try again')
            return redirect(url_for('user_login'))
        session['username'] = request.form['username']
        session['logged_in'] = True
        return redirect(url_for('index'))

    return render_template('login.html', form=form, title="Login")

# Routing - Logout

@app.route('/logout')
def logout():
    """Logs the user out and redirects to home"""
    session.clear()
    return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")))
 