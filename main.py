# Importing Flask,PyMongo

import os,env
from flask import Flask,render_template,redirect,request,url_for
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_DBNAME"] ="myCookBook"
app.config["MONGO_URI"] = os.environ.get('MONGO_URI', 'monogodb://localhost')



mongo = PyMongo(app)

# Routing

@app.route('/')
@app.route('/get_recipes')
def home():
          
    


 if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)
   