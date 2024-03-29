[Demo Here](https://pranita-cookbook.herokuapp.com/)

# Cookbook - Milestone Project 4 

<p>The data centric development module requires a project to be built using: MongoDB, HTML, CSS, JavaScript, Python and PyMongo. The project brief indicates to build a web application for a cookbook. The cookbook should allow the user to; browse through recipes, allow addition of recipes, allow removal of recipes, allow allergens and ingredients to be displayed. 

The user can add and delete recipes from the web application and filter according to allergen information and health information. Finally, a basic user and password registration will be added to the site for the user to access and login into the cookbook web application in order to edit and delete recipes they have added </p>
The user login and password application is not secure as the project brief does not cover this scope and authentication will be covered in the next module.

<strong>Please note this website is only for educational purposes to fulfil the criteria for Milestone 4 Data Centric Development Project </strong>
<hr>

## UX Design - User Experience

The recipe cookbook enables the user to; firstly ,view the; cooking time, serving and calories per recipe through flipping the card for each recipe. If the user wishes to proceed then can then; view the recipe instructions, search recipe using the search bar, filter diet and health labels for example; gluten-free and find recipes pertaining to filters. The diet labels pertain to dietary choices such as ; gluten-free, high-protein and balanced recipes. The health labels pertain to; vegan, vegetarian, sugar-conscious choices etc.
The registered users are able to login, add, edit and delete their own recipes without deleting those that have been added by the website author.
The website contains a navigation bar whereby the user can click on the 'cookbook logo' and return to the homepage. The navigation bar also contains; login, register, add (only once logged in) buttons.

The web application should fulfil the CRUD operations.

### Create

<p>The user should be able to create recipes through filling in the add recipe form which are then added to the back end of the database.</p>

### Read

<p> The non-logged in and non-registered user should be able to read the recipes as well as registered users. </p>


### Update

<p> The user should be able to edit their own recipes. If a user tries to edit or delete a recipe which is not their own, then a message is flashed in the alert box 'Asking the user to login'. Users can only update their own recipes. </p>


### Delete 

<p> The user should be able to delete their own recipes. </p>


### The User Interface

The user interface is simple and easy to understand with an image of the finished dish.

### Login and Register

<p> The user chooses a username which is unique to register otherwise an alert will flask up 'Sorry, username already taken. Please try another`. The user then chooses a password </p>
<p> The user must use the chosen username and password to login </p>

 Password hashing was implemented for security [werkzeug.security](https://werkzeug.palletsprojects.com/en/0.15.x/utils/#module-werkzeug.security) 

<hr>

## UX Design - User Stories

<p> A User should be able to : </p>
<ul>
<li> View the site from any device - should be responsive design in desktop, laptop, mobile and tablet views. </li>
<li> As a guest user (without a registered username or password) , all recipes should be allowed to be viewed in full which includes the ingredients and receipe method 'Get Cooking' button, search for a recipe, filter according to health and diet labels.</li>
<li> The user should quickly be able view the; cooking time, serving size and calories contained a recipe before clicking on to fully view the ingredients and get the instructions to cook.</li>
<li>  As a user recipes should filter for diet options : gluten free , sugar conscious, peanut free, alcohol free, vegan and vegetarian recipes which are all accessible through a drop down category selector. </li>
<li> As a user recipes  should filter for health options: low fat, low carbohydrate , high protein and low in sugar recipes which are all accessible through a drop down category selector.</li>
<li>  A user should be able to register and login to the site. </li>
<li> A user should be able to add and delete their own recipes once they are a registered user and have logged in.</li>
</ul>

<hr>

## Wire frames and Database Schema

<p> The wireframes for the Data Centric Development project were created using Balsamiq. Mocks-ups were produced for 
desktop and mobile versions.</p> 

[Wire Frames](static/wireframe/milestone_4_project.pdf)

<p> In this project before development I wanted to see how my database Schema would work. I devised a table as shown below. My developed site matches the database schema.</p>

[Database Schema](static/database_schema/database_schema.pdf)

## Features

###  Recipe Insertion

<p> The recipe were inserted through the import.py script. First a connection to the MongoDB database was made as indicated below and then the api through the api_key. The collection name and then the fields were inserted as indicated below. </p>

#### Config Vars

<p> AWS is connected to the database as below</p>

```
app = Flask(__name__)

MONGODB_URI= os.getenv("MONGO_URI")
DBS_NAME="myCookBook"
COLLECTION_NAME="recipes"

app.config["MONGO_URI"] = 'mongodb+srv://root:RootUser@myfirstdatabase-klrg6.mongodb.net/myCookBook?retryWrites=true'

mongo = PyMongo(app)

```

#### Collection Name set and Recipe insertion through API

<p> The fields below are inserted into the collection. The data is extracted through the api </p>

```
coll = conn[DBS_NAME][COLLECTION_NAME]

url = "https://api.edamam.com/search?q={}&app_id={}&app_key={}&from=1&to=2"
 
search = "steamed salmon" 

api_id="f69a50fd"

api_key="ef3a76518f0364a6f1958b13efcf06af"

r = requests.get(url.format(search,api_id,api_key)).json()

recipe = {
          'recipe': search,
          'recipe_name': r['hits'][0]['recipe']['label'],
          'recipe_image': r['hits'][0]['recipe']['image'],
          'serving_size': int(r['hits'][0]['recipe']['yield']),
          'diet_labels':r['hits'][0]['recipe']['dietLabels'],
          'health_labels': r['hits'][0]['recipe']['healthLabels'],
          'ingredients': r['hits'][0]['recipe']['ingredientLines'],
          'ingredients_raw': r['hits'][0]['recipe']['ingredients'],
          'calories': int(r['hits'][0]['recipe']['calories']),
          'cooking_time': r['hits'][0]['recipe']['totalTime'],
          'total_nutrients': r['hits'][0]['recipe']['totalNutrients'],
          'likes': {
              
          }
           }
```

#### Imported into Collection

<p> Through the pprint function, the data is inputted into the collection fields <p>

```
pprint(recipe)
i = input("Y/N: ")
if i == "Y":
    coll = mongo.db.recipe
    coll.insert_one(recipe)
```    


## Mongo DB

Mongo DB has been the choice of database use (document-orientated database) where data is stored in key and field format (JSON).
A database and collection created as below:

```database :myCookBook```
```collection:recipe```
```collection: user```

To main.py :

Config Vars added:

```app.config["MONGO_DBNAME"]= 'DBNAME'``` <br>
```app.config["MONGO_URI"] = mongosrv added ```


#### Collection - recipe

<p> The website contains a total of 12 recipes. The recipes have been inserted into the backend of the  MongoDB database using an import.py script which contains the fields below. A database has been created in MongoDB and then a collection name 'recipe'. The MongoDB collection contains the following fields:
<ul>
<li> recipe image - URL for recipe image inserted </li>
<li> ingredients - data type is 'string'</li>
<li> cooking time - data type is 'integar' </li>
<li> recipe_name - data type is 'string'</li>
<li> diet_name - data type is 'string' </li>
<li> health_labels - data type is 'string' </li>
<li> calories - data type is 'integar' </li>
<li> serving size  - data type is 'integar' </li>
<li> calories - data type is 'integar' </li>
<li> description - data type is 'string'</li>
</ul>

<p> It was decided at a later stage to not include full instructions of recipe preparation but use a 'Get Cooking' button which directs the user to a site where the recipe instructions are contained.
<ul>
<li> instructions - five fields - data type is 'string'</li>
</ul>

#### Collection - user

When users register, there usernames are stored into the collection user in the database. Once a recipe is created or deleted by the user, this will also delete and update in the database.

<hr>

### Search and Filter
There is at least one recipe pertaining to one health label option or diet label option. The user can select the 'up arrow' on each recipe to quickly view the: time taken to prepare, serving size and number of calories in that particular recipe. The user can then decide to whether to view the recipe which contains: a description of the dish, cooking time, serving size and calories indicated, instructions on how to prepare the dish and an image of the finished dish.
The navigation bar contains the title of the cookbook 'Pranita's cookbook' and enables the user to click on the 'cookbook logo' to return to the homepage.

Two main search options exist:

<ol>
<li> Search Box : User is able to search by typing in a recipe name e.g 'Bhindi Kadhi' to filter through the 12 recipes to bring up the chosen recipe.</li><br>
<li> Filter Options: User can filter using diet and health labels to choose the options presented.</li>
</ol>
</p>
<hr>

### Pagination
<p> There is a maximum of 6 recipes per page with a total of 12. The user is able to move to the next set of 6 recipes using the pagination tab at the bottom of the page, thereby moving between pages 1 and 2.<p>


## Features left to implement
<ol>
<li> A reset password facility whereby users can reset their passwords if they have forgotten them </li>
</ol>

<hr>

## Technologies Used

<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5"> HTML5 </a> HTML 5 was used to create the structure of webpage with the necessary elements.</li>
<li><a href="https://www.w3.org/Style/CSS/Overview.en.html"> CSS3 </a> CSS3 was used to write custom css style the webpage with the necessary attributes.</li>
<li><a href="https://materializecss.com/"> Materilaize 1.0.0 </a> The Materilize framework is used to style the webpage alongside custom css and the grid system is adhered to.</li>
<li><a href="https://jquery.com/"> Jquery </a> Jquery was used to create the collapsible navbar in toggle mode for mobile devices.</li>
<li><a href="https://www.javascript.com/"> Javascript </a>Javascript was used to create a scroll button to redirect the user back to the top of the website.</li>

<li><a href ="https://validator.w3.org/">WC3 Markup Validation service</a> WC3 was used to validate html code.</li>
<li><a href ="https://jigsaw.w3.org/css-validator/">WC3 CSS Validation service</a> WC3 CSS was use to validate css code.</li>
<li><a href ="https://www.python.org/dev/peps/pep-0008/">PEP8</a> PEP8 was installed and used to validate Python code.</li>

<li> <a href ="https://www.python.org/">Python</a>Python is used for the back-code to fulfil the 'GET' and 'POST' requests and import.</li>
<li> <a href = "https://git-scm.com/">Git</a>Git was used to push the files to the local repository.</li> 
<li><a href="https://www.heroku.com/">Heroku</a>Heroku is use to deploy sites using Python.</li>
<li><a href ="https://www.mongodb.com/">MongoDB</a>MongoDB is a nonSQL based database whereby recipes are inserted using the import.py script into the respective collection once a database is set up.</li>
</ul>

## Framework 

<a href="https://materializecss.com/">Materilize</a> - The Materilize framework is used to style the webpage alongside custom css and the grid system is adhered to.


## Testing and Validating

### Validating Code

The HTML and CSS3 codes were validated on WSC validator and no syntax errors were found. The Javascript/Jquery codes were validated using JS Hint and no errors were found. 

The Python code was validated on PEP8 and no errors were found.
PEP 8 was installed using the bash command:
```$ pip install pep8```
Bash Command line:
```$ pep8 --first main.py``` was used to indicate errors in the python code and erros were subsequently rectified.

### Responsive Design Testing

The website was tested at various screen sizes which include mobile and tablet devices.   
The website has been found to be fully functional and has been tested on the following browsers:

<ul>
<li> Google Chrome </li>
<li> Microsoft Edge </li>
<li> Mozilla Firefox </li>
<li> Opera </li>
</ul>

The website was tested on the following devices and the website was found to display all the coded elements and attributes:

<ul>
<li> Desktop </li>
<li> Laptop with HiDPI</li>
<li> Laptop with MDPI </li>
<li> Pixel 2 </li>
<li> Pixel 2L </li>
<li> Galaxy S5 </li>
<li> iPhone 5/SE </li>
<li> iPhone 6/7/8 </li>
<li> iPhone 6/7/8 plus </li>
<li> iPhone X </li>
<li> iPad </li>
<li> iPad Mini </li>
<li> iPad Pro </li>
</ul> 

### Responsive Design Testing

<p> On mobile view the responsive design fits the user stories as the diet and health labels filter search stack on top of each other , alongside the recipes below. The toggle button is functional with users able to select login or register. The website is functional and visible in mobile view.</p>
<p> On large screen view, tablet and laptop view the website is functional and fully visible without compromising pixilation in images.</p>
    


## Testing User Stories

<p> A potential user/user is able to view the recipes fully with instructions without registering and logging in. A registered and logged in user has the
additional benefit of : adding, deleting and editing their recipes. The recipes which have been imported by author of the website are protected from being deleted.
The user is able to filter recipes through the diet and health filters and search for a recipe through the search box.</p>

#### CRUD operations testing

##### Create
<p> The logged in user is able to create recipes through the add recipe form once logged in. </p>

##### Read

<p> The user is able to click on the cards of each recipe and quickly view ; cooking time, serving size and calories of each recipe. The user is able to view recipes fully. </p>

##### Update
<p> The logged in user is able to edit their own  added recipes. </p>

##### Delete
<p> The logged in user to able to delete their own recipes. </p>


<hr>

## Deployment

#### IDE

The IDE used to write the code for the website  was AWS Cloud 9 student account : https://www.awseducate.com/student/s/awssite

#### Git and GitHub

The code was pushed to a local repository created in Git Hub using git commands [Milestone_4_cookbook](https://github.com/pranitastudent/Milestone_4_cookbook)

##### Running the project from GitHub

<ol>
<li> Manually download the project from Github and upload to the IDE fo choice. </li>
<li> Create a requirements txt file using the command:</li>

   ``` sudo pip3 freeze -- local > requirements.txt ``` 
   
 <li> Set up environment variables to run the app.</li>

     app.config["MONGO_DBNAME"] = "myCookBook" 
     
     app.config["MONGO_URI"] = 'mongodb+srv://root:RootUser@myfirstdatabase-klrg6.mongodb.net/myCookBook?retryWrites=true' 
     
     app.config['SECRET_KEY'] = SECRET_KEY 

<li> Enter the command in the bash terminal : 

``` python3 main.py ``` to run the app.  </li>

</ol>

##### Running the Project from CLI


<ol>
<li> Clone the repository: 

   ``` https://github.com/pranitastudent/Milestone_4_cookbook.git ``` </li>
<li> Create a requirements txt file using the command:</li>

   ``` sudo pip3 freeze -- local > requirements.txt ``` 
   
 <li> Set up environment variables to run the app.</li>

     app.config["MONGO_DBNAME"] = "myCookBook" 
     
     app.config["MONGO_URI"] = 'mongodb+srv://root:RootUser@myfirstdatabase-klrg6.mongodb.net/myCookBook?retryWrites=true' 
     
     app.config['SECRET_KEY'] = SECRET_KEY 

<li> Enter the command in teh bash terminal : 

``` python3 main.py ``` to run the app.  </li>

</ol>


### Deploying to Heroku

<strong> The code was deployed to Heroku as Heroku supports Python platforms while Github only hosts static sites. </strong>

Name of app: pranita-cookbook
[URI](https://pranita-cookbook.herokuapp.com/)

The bash command used is:

``` heroku login ```
<ol>
<li> A requirements.txt file is created as Heroku deployment requiries the dependencies. </li>

The bash command used is :

``` sudo pip3 freeze -- local > requirements.txt ```

<li> A Procfile is required to be created so that Heroku recognises the Python3 language. </li>

The bash command used is :

``` sudo pip3 > Procfile ```

A git repository is initialised

``` git init ```

```heroku:git: remote -a pranita-cookbook ``` 

Files are them added and committed

The bash command to push the code to Heroku is :

``` git push heroku master ```

<li> The config vars need to be set up in Heroku with the relevant IP and Port Settings: </li>

pranita-cookbook > settings > Reveal  Config Vars:

``` IP: 0.0.0.0```

```PORT : 5000```

<li> pranita-cookbook > Open App </li>

The app is finally deployed at [pranita-cookbook](https://pranita-cookbook.herokuapp.com/)

</ol>




<hr>

## Credits

### Content

The recipes and recipe images were imported from the [ Edamam API](https://developer.edamam.com/)

### Recipe Instructions

##### Page 1 Recipes 

[Bhindi Khadhi](https://www.cookwithmanali.com/bhindi-kadhi/) <br>
[Roti Jala](https://www.seriouseats.com/recipes/2011/08/roti-jala-malaysian-pancake-recipe.html)<br>
[Vegetarian Lasagna](https://www.bbcgoodfood.com/recipes/10603/roasted-vegetable-lasagne)<br>
[BLT Burger](https://www.delish.com/cooking/recipe-ideas/recipes/a47639/blt-burger-recipe/)<br>
[Kimchi Pasta with Bacon and Seasome Seeds](https://www.seriouseats.com/recipes/2012/01/kimchi-pasta-with-bacon-and-sesame-seeds.html)<br>
[Asparagus Rissoto](https://www.bbc.co.uk/food/recipes/asparagusrisotto_85593)<br>

##### Page 2 Recipes

[Matzo Ball Soup](https://greatamericanturkeyco.com/blogs/recipes/bubbe-s-tasty-turkey-matzo-ball-soup-bubbes-tasty-turkey-matzo-ball-soup)<br>
[Saag Aloo](https://www.bbcgoodfood.com/recipes/sag-aloo)<br>
[Aubergine Melts](https://www.bbcgoodfood.com/recipes/2213/aubergine-melts)<br>
[Chicken, sweet potato and coconut curry](https://www.bbcgoodfood.com/recipes/1555/chicken-sweet-potato-and-coconut-curry)<br>
[Daal Saag](https://www.bbc.co.uk/food/recipes/daalsaag_74848)<br>
[Steamed Salmon](https://www.jamieoliver.com/recipes/fish-recipes/super-speedy-steamed-salmon/)<br>

#### WS Schools Code

The code for the back-to-the top button was adapted from WS Schools site

[WS Schools Back to the top button](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp)

#### Stack Overflow code

The code for the secret key in main.py lines 19 and 20 was taken from the stack overflow site question page

[Stack Overflow Code](https://stackoverflow.com/questions/34902378/where-do-i-get-a-secret-key-for-flask/34903502)

<hr>

### Acknowledgements

<p> I would like to thank The Code Institute for teaching me back-end coding as well as front-end coding notably; HTML, CSS, jQuery, Python and how to use MongoDB and PyMongo. I would like to thank the tutors and my mentor Ali Ashik for their helpful input into my queries.</p>



