[Deployed Site](https://pranita-cookbook.herokuapp.com/)

# Cookbook - Milestone Project 4 

<p>The data centric development module requires a project to be built using : MongoDB, HTML, CSS, JavaScript , Python and PyMongo. The project brief indicates to build a web application for a cookbook. The cookbook should allow the user to browse through recipes, allow addition of recipes , allow allergens and ingredients to be displayed. 

The user is able to add and delete recipes from the web application and filter according to allergen information and health information. Finally a basic user and password registration will be added to the site for the user to access and login into the cookbook web application in order to edit and delete recipes they have added </p>
The user login and password application is not secure as the project brief does not cover this scope.

<strong>Please note this website is only for educational purposes to fulfil the criteria for Milestone 4 Data Centric Development Project </strong>
<hr>

## User Experience

The recipe cookbook enables the user to; firstly, view the; cooking time, serving and calories per recipe, then view the recipe instructions, search recipe using the search bar, filter diet and health labels for example; gluten-free and find recipes pertaining to filter.
The registered users are able to login, add, edit and delete their own recipes without deleting those that have been added by the website author.
The website contains a navigation bar whereby the user can click on the 'cookbook logo' and return to the homepage. The navigation bar also contains; login, register, add (only once logged in) buttons.

The user interface is simple and easy to understand with an image of finished dish.


<hr>

## User Stories

<p> A User should be able to : </p>
<ul>
<li> View the site from any device - should be responsive design. </li>
<li> As a guest user (without a registered username or password) , all recipes should be allowed to be viewed in full which includes the ingredients and instructions, search for a recipe, filter according to health and diet labels and view instructions on how to cook that particular recipe.</li>
<li>  As a user recipes should filter for : gluten free , sugar conscious, peanut free, alcohol free, vegan and vegetarian recipes which are all accessible through a drop down category selector. </li>
<li> As a user recipes  should filter for the health category : low fat, low carbohydrate , high protein and low in sugar recipes which are all accessible through a drop down category selector.</li>
<li>  A user should be able to register an login to the site. </li>
<li> A user should be able to add and delete recipes once they are a registered user and have logged in.</li>
</ul>

<hr>

## Wire frames

<p> The wireframes for the Data Centric Development project were created using Balsamiq. Mocks-ups were produced for 
desktop and mobile versions.</p> 

[Wire Frames](static/wireframe/milestone_4_project.pdf)

## Features

###  Recipe Insertion
<p> The website contains a total of 12 recipes. The recipes have been inserted into the backend of the  MongoDB database using an import.py script which contains the fields below. A database has been created in MongoDB and then a collection name 'recipe The MONGODb collection contains the following fields:
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

<p> It was decided at a later stage to include full instructions of recipe preparation rather than direct the user to an alternative site using a button linked to. There following additional fields were added below to the collection:  </p>

<ul>
<li> instructions - five fields - data type is 'string'</li>
</ul>
<hr>

### Search and Filter
There is at least once recipe pertaining to one health label option or diet label option. The user can select the 'up arrow' on each recipe to quickly view the: time taken to prepare, serving size and amount of calories in that particular dish. The user can then decide to whether view the recipe which contains: a description of the dish, cooking time, serving size and calories indicated, instructions on how to prepare the dish and an image of the finished dish.
The navigation bar contains the title of the cookbook 'Pranita's cookbook' and enables the user to click on the 'cookbook logo' to return to the homepage.

Two main search options exist:

<ol>
<li> Search Box : User is able to search by typing in a recipe name e.g 'Bhindi Kadhi' to filter through the 12 recipes to bring up the chosen recipe.</li><br>
<li> Filter Options: User can filter using Diet and Health labels to choose the options presented. They can only filter for one option at time. </li>
</ol>
</p>
<hr>

### Pagination
<p> There is a maximum of 6 recipes per page with a total of 12. The user is able to move to the next set of 6 recipes using the pagination tab at the bottom of the page, thereby moving between pages 1 and 2.<p>


## Features left to implement
<ol>
<li> A reset password facility whereby users can reset there passwords if they have forgotten them </li>
<li> Users to be  select multiple options from both the diet and health tabs and be able to search recipes based on these </li>
</ol>

<hr>

## Technologies Used

<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5"> HTML5 </a></li> HTML 5 was used to create the structure of webpage with the necessary elements.</li>
<li><a href="https://www.w3.org/Style/CSS/Overview.en.html"> CSS3 </a></li> CSS3 was used to write custom css style the webpage with the necessary attributes.</li>
<li><a href="https://materializecss.com/"> Materilaize 1.0.0 </a> </li>  The Materilize framework is used to style the webpage alongside custom css and the grid system is adhered to.</li>
<li><a href="https://jquery.com/"> Jquery </a></li> Jquery was used to create the collapsible navbar in toggle mode for mobile devices and for smooth scroll of the website.</li>
<li> <a href ="https://www.python.org/">Python</a></li> Python is used for the back-code to fullfil the 'GET' and 'POST' requests and import.</li>
<li> <a href = "https://git-scm.com/">Git</a></li> Git was used to push the files to the local repository.</li> 
<li><a href="https://www.heroku.com/">Heroku</a><li>Heroku is use to deploy sites using Python.</li>
<li><a href ="https://www.mongodb.com/">MongoDB</a></li>MongoDB is the database whereby recipes are inserted using the import.py script into the respective collection once a database is set up.</li>
</ul>

## Framework 
<ul>
<li><a href="https://materializecss.com/"> </a></li> The Materilize framework is used to style the webpage alongside custom css and the grid system is adhered to.
</ul>

## Testing and Validating


The HTML and CSS3 codes were validated on WSC validator and no syntax errors were found. The Jquery was validated using JS Hint and no errors were found.  The Python code was validated on PEP8 and no errors were found.The website was tested at various screen sizes which include mobile and tablet devices.   
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


### Coding Bugs

<p> During the coding process of the project there were two main bugs encountered : </p>

#### Search Box Error

<p> When the 'Go' button is pressed in teh search filed the following erros appears which I have been Unable to resolve 'TypeError:if no direction is specified, key_or_list must be an instance of list'</p>

```line 55: total = mongo.db.recipe.create_index({'$text':{'$search': db_query }})```

<p> It was specuated that a syntax error maybe causing this error  for example (code from the site below:
[MongoDB site](https://jira.mongodb.org/browse/PYTHON-953)

Code : ```db.collection.create_index({"$**": "text"})```
Code replaced : ```db.collection.create_index([('$**', 'text')])```

This however did not resolve the problem. </p>

In order to resolve theis error, the question as asked on [stackoverflow.com](https://stackoverflow.com/questions/56506781/how-to-fix-typeerror-if-no-direction-is-specified-key-or-list-must-be-an-inst)
<p> The solution provided by a user on stackoverflow was :

Code ```receip.find({keyword: request.query.keyword, active: true})``` was also found to not work despite the insertion of the keyword.

The error unfortunately breaks the site and the user would have to reload the site.

</p>

#### Reselecting once options have been selected

<p> The user is unable to select the options again , once these have been selected </p>


## Testing User Stories

<p> A potential user/user is able to view the recipes fully with instructions without registering and logging in. A registered and logged in user has the
additional benifit of : adding, deleting and editing their recipes. The recipes which have been imported by author of the website are protected from being deleted.
The user unfortunately is not able to reselect the filter options once selected and filtered.  The user is not able to search for a recipe due to the
the 'TypeError' mentioned in 'Coding Bugs'.</p>

<hr>

## Deployment

The IDE used to write the code for the website  was AWS Cloud 9 student account : https://www.awseducate.com/student/s/awssite
The code was pushed to a local repository created in Git Hub using git commands [Milestone_4_cookbook](https://github.com/pranitastudent/Milestone_4_cookbook)

The code was deployed to Heroku as Heroku supports Python plateforms while Github only hosts static sites.  A Procfile and requirements.txt files were created using the ```sudo pip3`` command.
'sudo pip3' commands.

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

<hr>

### Acknowledgements

<p> I would like to thank The Code Institute for teaching me back-end coding as well as front-end coding notably; HTML, CSS, jQuery, Python and how to use MongoDB and PyMongo. I would like to thank the tutors for their helpful input to my queries too.</p>



