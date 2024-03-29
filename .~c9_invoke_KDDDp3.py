# Importing - Setup Flask

import os
import math
import re
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from forms import LoginForm, RegistrationForm, RecipeForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, redirect, request, url_for, flash
from flask import session

#  App Config
app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'myCookBook'
app.config["MONGO_URI"] = 'mongodb+srv://root:RootUser@myfirstdatabase-klrg6.mongodb.net/myCookBook?retryWrites=true'

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


mongo = PyMongo(app)

# Routing

# Index Page


@app.route('/')
def index():
    """
    Route lets users see all recipes
    """

    page_limit = 6  # Logic for pagination
    current_page = int(request.args.get('current_page', 1))
    total = mongo.db.recipe.count()
    pages = range(1, int(math.ceil(total / page_limit)) + 1)
    recipes = mongo.db.recipe.find().sort('_id', pymongo.ASCENDING).skip((current_page - 1)*page_limit).limit(page_limit)
    return render_template('index.html', recipe=recipes, title='Home', current_page=current_page, pages=pages)

# Viewing Recipe Route


@app.route('/recipe/<recipe_id>', methods=['GET', 'PUT'])
def recipe(recipe_id):
    """
    Route for viewing a single recipe in detail.
    Logged in users can edit and delete.
    """
    a_recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    return render_template('recipe.html',
                               recipe=a_recipe, title=a_recipe['recipe_name'])


@app.route('/profile/<user_id>')
def profile_page(user_id):
    """Route for users to view their profile page"""
    if 'logged_in' not in session:  # Check if its a logged in user
        flash('Sorry, only logged in users can view the profile page. Please register')
        return redirect(url_for('index'))
    current_user = mongo.db.user.find_one({"_id": ObjectId(user_id)})
    recipes = mongo.db.recipe.find({'username': current_user['name']}).sort('_id', pymongo.ASCENDING)
    count = mongo.db.recipe.find({'username': current_user['name']}).count()
    return render_template('profile.html', current_user=current_user, recipes=recipes, count=count, title="Profile Page")


#  Search for Recipe Route

@app.route('/search')
def search():
    # Route for full text search bar
    page_limit = 6  # Logic for pagination
    current_page = int(request.args.get('current_page', 1))
    db_query = request.args['db_query']
    total = mongo.db.recipe.find({'$text': {'$search': db_query}})
    results = mongo.db.recipe.find({'$text': {'$search': db_query}}).sort('_id', pymongo.ASCENDING).skip((current_page - 1)*page_limit).limit(page_limit)
    return render_template('search.html', results=results, current_page=current_page, db_query=db_query, title="Search Results")
        
# Filter search Route


@app.route('/filtered_search', methods=['GET', 'POST'])
def filtered():
    if request.method == "POST":
        for i in request.form:
            if i == "diet_labels":
                filter_items = []
                items = request.form.getlist('diet_labels')  # get as a list []
                my_key = request.form  # get as a multdict
                for item in items:  # iterate through the list
                    for key in my_key:  # grab key_name
                        filter_items.append({key: item})
                        results = mongo.db.recipe.find({
                                            '$and': [{'$or': filter_items}]})
                total_results = mongo.db.recipe.find({
                                    '$and': [{'$or': filter_items}]}).count()
                return render_template('filter.html',
                                           title="Filtered Search",
                                           results=results,
                                           total_results=total_results)
    if request.method == "POST":
        for i in request.form:
            if i == "health_labels":
                filter_items = []
                items = request.form.getlist('diet_labels')  # get as a list []
                my_key = request.form  # get as a multdict
                for item in items:  # iterate through the list
                    for key in my_key:  # grab key_name
                        filter_items.append({key: item})
                        results = mongo.db.recipe.find({
                                            '$and': [{'$or': filter_items}]})
                total_results = mongo.db.recipe.find({
                                    '$and': [{'$or': filter_items}]}).count()
                return render_template('filter.html',
                                           title="Filtered Search",
                                           results=results,
                                           total_results=total_results)
                
                                                             


# Create Recipes Route


@app.route('/create_recipe', methods=['GET', 'POST'])
def create_recipe():
    """Create a new recipe to db collection"""
    if 'logged_in' not in session:  # Check if its a logged in user
        flash('Sorry, only logged in users can create recipes. Please register')
        return redirect(url_for('index'))

    form = RecipeForm(request.form)  # Initialise the form
    user = mongo.db.user.find_one({"name": session['username'].title()})
    
    if form.validate_on_submit():  # Insert new recipe if form is submitted
       recipes = mongo.db.recipe
       recipes.insert_one({
        'recipe': request.form['recipe_name'],
        'recipe_name': request.form['recipe_name'],
        'recipe_image': request.form['recipe_image'],
        'serving_size': int(request.form['serving_size']),
        'diet_labels': request.form['diet_labels'],
        'health_labels': request.form['health_labels'],
        'ingredients': request.form['ingredients'],
        'calories': request.form['calories'],
        'cooking_time': request.form['cooking_time'],
        'description': request.form['description'],
        'source': request.form['source'],
        'username': session['username'].title(),
         })
       flash('Recipe Added!')
       return redirect(url_for('index'))
    return render_template('add_recipe.html', form=form, title="Add Recipe")
    
# Edit Recipe Route


@app.route('/edit_recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    """Function to edit seclect recipe"""
    if 'logged_in' not in session:  # Check if its a logged in user
        flash('Sorry, only logged in users can create recipes. Please register')
        return redirect(url_for('index'))
    
    user = mongo.db.user.find_one({"name": session['username'].title()})
    the_recipe = mongo.db.recipe.find_one_or_404({'_id': ObjectId(recipe_id)})
    form = RecipeForm()
    
    if user['name'].title() == the_recipe['username'].title():  # If user created then user can edit
        if request.method == 'GET':
            form = RecipeForm(data=the_recipe)
            return render_template('edit_recipe.html', recipe=the_recipe, form=form, title="Edit Recipe")
        if form.validate_on_submit():
            recipe = mongo.db.recipe
            recipe.update_one({
                '_id': ObjectId(recipe_id),
            }, {
                '$set': {
                             'recipe': request.form['recipe_name'],
                             'recipe_name': request.form['recipe_name'],
                             'recipe_image': request.form['recipe_image'],
                             'serving_size': int(request.form['serving_size']),
                             'diet_labels': request.form['diet_labels'],
                             'health_labels': request.form['health_labels'],
                             'ingredients': request.form['ingredients'],
                             'calories': request.form['calories'],
                             'cooking_time': request.form['cooking_time'],
                             'description': request.form['description'],
                             'source': request.form['source']
                                                          }})
            flash('Recipe updated.')
            return redirect(url_for('recipe', recipe_id=recipe_id))
    flash("Sorry this is not your recipe to edit!")  # In case a user tried to enter URL manually
    return redirect(url_for('recipe', recipe_id=recipe_id))
    
# Delete  Recipe Route


@app.route('/delete/<recipe_id>')
def delete_recipe(recipe_id):
    """Function for deleting a single recipe"""
    if session:
        user = mongo.db.user.find_one({"name": session['username'].title()})
        the_recipe = mongo.db.recipe.find_one_or_404({'_id': ObjectId(recipe_id)})

        if user['name'].title() == the_recipe['username'].title():  # If user created then user can delete
            recipe = mongo.db.recipe
            recipe.delete_one({
                '_id': ObjectId(recipe_id)
            })
            flash('Recipe deleted')
            return redirect(url_for('index'))
            
        flash("Sorry this is not your recipe to edit!")   # In case a user tried to enter URL manually
        return redirect(url_for('recipe', recipe_id=recipe_id))
    else:
        flash('Sorry, only logged in user can view this page')
        return redirect(url_for('index'))
        
# Add Likes to each Recipe


@app.route('/i-made-it/<recipe_id>')
def i_made_it(recipe_id):
    """ Function to increment the counter i-made-it counter"""
    mongo.db.recipe.find_one_and_update(
        {'_id': ObjectId(recipe_id)},
        {'$inc': {'i-made-it': 1}})
    return redirect(url_for('recipe', recipe_id=recipe_id)) 
    
    
# Registration Route


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Function for handling the registration of users"""
    if 'logged_in' in session:  # Check is user already logged in
        return redirect(url_for('index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
            
        user = mongo.db.user
        dup_user = user.find_one({'name': request.form['username'].title()})
            
        if dup_user is None:
            hash_pass = generate_password_hash(request.form['password'])
            user.insert_one({'name': request.form['username'].title(),
                             'pass': hash_pass})
            session['username'] = request.form['username']
            session['logged_in'] = True
            return redirect(url_for('index'))
        flash('Sorry, username already taken. Please try another.')
        return redirect(url_for('register'))
    return render_template('register.html', form=form, title="Register")

# Login Route


@app.route('/login', methods=['GET', 'POST'])
def user_login():
    """Function for handling the logging in of users"""
    if 'logged_in' in session: 
        return redirect(url_for('index'))
    form = LoginForm()

    if form.validate_on_submit():
        user = mongo.db.user
        logged_in_user = user.find_one({'name': request.form['username'].title()})
        
        if logged_in_user:
            if check_password_hash(logged_in_user['pass'],
                                   request.form['password']):
                session['username'] = request.form['username']
                session['logged_in'] = True
                return redirect(url_for('index'))
            flash('Sorry incorrect password!')
            return redirect(url_for('user_login'))
    return render_template('login.html', form=form, title='Login')

# Logout Route


@app.route('/logout')
def logout():
    """Logs the user out and redirects to home"""
    session.clear()
    return redirect(url_for('index'))
    
# Error Handling


@app.errorhandler(404)
def page_not_found(e):
    """ Route for handling errors"""
    return render_template('404.html', title="Page not found!"), 404

    
@app.errorhandler(500)
def internal_server_error(e):
    """Route for hadnling 500 server error"""
    return render_template('500.html', title="Internal Server Error"), 500


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=False)