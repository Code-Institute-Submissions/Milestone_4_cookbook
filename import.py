# Import pymongo

from flask_pymongo import PyMongo, pymongo, mongo
from flask import Flask

# Import python os module

import os
import requests
from pprint import pprint

# config vars
app = Flask(__name__)
MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myCookBook"
COLLECTION_NAME = "recipes"


mongo = PyMongo(app)

# Connecting to database


def mongo_connect(url):

    try:
        conn = pymongo.MongoClient(url)
        print('Mongo is connected')
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print('Could not connect to MongoDB: %s') % e

# Assigning our connection to connect to MongoDB


conn = mongo_connect(MONGODB_URI)

# Connection

coll = conn[DBS_NAME][COLLECTION_NAME]
url = "https://api.edamam.com/search?q={}&app_id={}&app_key={}&from=1&to=2"
search = "steamed salmon"
api_id = "f69a50fd"
api_key = "ef3a76518f0364a6f1958b13efcf06af"

r = requests.get(url.format(search, api_id, api_key)).json()

recipe = {
          'recipe': search,
          'recipe_name': r['hits'][0]['recipe']['label'],
          'recipe_image': r['hits'][0]['recipe']['image'],
          'serving_size': int(r['hits'][0]['recipe']['yield']),
          'diet_labels': r['hits'][0]['recipe']['dietLabels'],
          'health_labels': r['hits'][0]['recipe']['healthLabels'],
          'ingredients': r['hits'][0]['recipe']['ingredientLines'],
          'ingredients_raw': r['hits'][0]['recipe']['ingredients'],
          'calories': int(r['hits'][0]['recipe']['calories']),
          'cooking_time': r['hits'][0]['recipe']['totalTime'],
          'total_nutrients': r['hits'][0]['recipe']['totalNutrients'],
          'likes': {
          }
           }
#  Adding Recipe from API to MongoDB

pprint(recipe)
i = input("Y/N: ")
if i == "Y":
    coll = mongo.db.recipe
    coll.insert_one(recipe)               