# Importing Flask,PyMongo

import os,env
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_DBNAME"] ="myCookBook"
app.config["MONGO_URI"] = os.environ.get('MONGO_URI', 'monogodb://localhost')
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')



mongo = PyMongo(app)

# Routing

@app.route('/')
@app.route('/get_recipes')
def index():
    recipe = mongo.db.recipe.find()
    return render_template('index.html', recipe=recipe, title="Home"
    
# Routing - Registration of login    
    
@app.route('/register', methods=['GET', 'POST'])
def register():
 
 if session.get('logged_in'):
        if session['logged_in'] is True:
            return redirect(url_for('index'))

    form = RegistrationForm()


 
   
  



   
          
    


 if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)
   