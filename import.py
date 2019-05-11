# Import pymongo

import pymongo

# Import python os module

import os, requests
from pprint import pprint

# config vars

MONGODB_URI= os.getenv("MONGO_URI")
DBS_NAME="myCookBook"
COLLECTION_NAME="recipe"

# Coonecting to database

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print('Mongo is connected')
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print('Could not connect to MongoDB: %s') % e

# Assigning our connection to connect to MongoDB

conn = mongo_connect(MONGODB_URI)

# Set Collection name 

coll = conn[DBS_NAME][COLLECTION_NAME]

url = "https://api.edamam.com/search?q={}&app_id={}&app_key={}&from=1&to=2"
 
search = "sushi" 

api_id="f69a50fd"

api_key="ef3a76518f0364a6f1958b13efcf06af"

r = requests.get(url.format(search,api_id,api_key)).json()

