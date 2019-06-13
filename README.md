# The Digital Kitchen , the online cookbook for everyone who likes to cook and to share their recipes #
This website is available to view here - https://the-digital-kitchen.herokuapp.com/index -

## UX ##
This web application is made for users who would like to store and easily access cooking recipes of different cuisines, categories, ingredients and difficulties. 
My target market could include anyone of any age group, but more specifically, this application is made for people who enjoy cooking, learning new recipes and wanting to share their own recipes with the online community. 
This type of user will want to be able to have their own account where they can add, edit or delete any of their recipes, view recipes of different ingredients, categories and also explore different cuisines. 
This user will also want to be able to know which main ingredients there are in these recipes, and how long these recipes will take to prepare and complete. 
My project is a suitable way of achieving this because it provides a form for the user to use when signing in or registering onto the application and functions which will allow the user to create and update their own recipes, as well as delete them.

General User Stories:

* As a user type, I want to be able to create an account with my own username and password, and login with these credentials each time I want to access the application.
* As a user type, I would like to be able to login and create my own recipes.
* As a user type, I would like to be able to view a recipe based on the cuisine, category or main ingredient.

Real Life User Stories:

* User 1: I'd like my username to be 'BASTIAAN' and would also like to have my own password when logging in.
* User 2: I would like to be able to find a variety of vegetarian recipes.
* User 3: I would like to be able to select certain categories or ingredients whilst creating a recipe.

## Features ##
* Login/Register form - this will allow the user to either log into an existing account or create a new account, inserting them into the database.
* Add/edit recipe form - this will allow logged in users to either create a new recipe (which will be inserted into the database) or edit one of their own existing recipes (which will be updated).
* Delete recipe function - this will allow the logged in user to delete one of their own recipes, completely removing it from the database.
* Filter by category, cuisine, main ingredient - this will allow the user to sort recipes by these filters, directing them to a page displaying these sorted recipes.
* Filter by cuisine - this will allow the user to be shown all recipes from a specific cuisine which they have chosen from the homepage.
* Log out - this will allow the user to log out of the current session, also providing them the option to return to the homepage or log back in.

### Existing Features ###
* Register form allows User 1 to create their chosen username 'BASTIAAN' and have a password of their choice which they can use to log in.
* Filters on homepage allow User 2 to find vegetarian recipes.
* Add/edit recipe form allows User 3 to create their recipe. They can then view this in 'My Recipes' and 'All Recipes'.
* Delete recipe function allows all users to delete their own recipes, however, at this point in time, any user can delete any other user's recipes which is one disadvantage.
* Logout allows all users to log out of their current sessions, providing them the options to return to homepage or log back in.

### Future Features ###
* Like/Dislike recipe - this feature would allow the user to like or dislike any recipe. The results of these likes and dislikes would then be displayed on a graphical chart.
* Favourite a recipe - this feature would allow the user to save their favourite recipes and view them under 'Favourite Recipes'.
* Most popular/most recent recipes - this feature will display most popular/most recent recipes based on how many likes the recipe received or how recently the recipe was created.

## Technologies Used ##
* [HTML5](https://www.w3schools.com/html/ "HTML5")
This project uses HTML to build the foundation of the web application and includes links to Materialize, Materialize JS, CSS, and Font Awesome.

* [CSS](https://www.w3schools.com/css/ "CSS")
This project uses CSS to style the features of the web application, including the header, footer and each page of the Digital Kitchen.

* [JavaScript](https://www.javascript.com/ "JavaScript")
This project uses JavaScript for interactive functionality of the application.

* [Python](https://www.python.org/ "Python")
This project uses Python to provide the backend functionality of the Digital Kitchen, including functions to add, edit or delete a recipe.

* [PyMongo](https://api.mongodb.com/python/current/ "PyMongo")
This project uses PyMongo which is a MongoDB driver for Python, used to access the MongoDB database.

* [MongoDB Atlas](https://www.mongodb.com/cloud/atlas "MongoDB Atlas")
This project uses MongoDB Atlas to host the database for the application in the cloud.

* [Flask](http://flask.pocoo.org/ "Flask")
This project uses the Flask microframework to bring the frontend and backend of the application together.

* [jQuery](https://jquery.com/ "jQuery")
This project uses jQuery which is included with Materialize to initialise many of the Materialize components used within the application (script found in base.html).

* [Font Awesome](https://fontawesome.com/ "Font Awesome")
This project uses Font Awesome to provide icons for the application.

* [Google Fonts](https://fonts.google.com/ "Google Fonts")
This project uses Google Fonts to provide fonts for the headings of the web application.

## Testing ## 

### Manual Tests ###
This web application has been manually tested with different scenarios that the user may experience.

Sign In

* Click on 'Sign In' in the header or in the welcome card and be directed to 'signin.html'.
* Sign in with username 'USER1' and password 'user1'.
* Click on 'Sign In' and be directed back to the homepage.
* Check the user is logged in by seeing if 'Add Recipe' and 'My Recipes' are available in the navigation.

Register

* Click on 'Register' in the header or in the welcome card and be directed to 'register.html'.
* Choose a username and password of your choice.
* Click on 'Register' and be redirected to 'home.html'.
* Check the user is logged in by seeing if 'Add Recipe' and 'My Recipe' are available in the navigation.

Homepage

* Click on the brand logo in the top-left corner of the page or click on 'Home' in the navigation bar.
* Be directed to 'home.html'.

Recipes By Cuisine

* From the homepage, choose a cuisine and be shown cuisine description and a button to view all recipes by chosen cuisine.

All Recipes

* Choose 'All Recipes' in the navigation bar and be directed to 'allrecipes.html'.
* Be shown all recipes in the database on one page.
* Be shown recipe description and details when card is clicked on.

View Recipe

* Click on 'View Recipe'
* Be directed to the get_recipe page and be shown all details of the recipe, including the ingredients, method and image.

Add Recipe

* If username is in session, be directed to 'addrecipe.html'.
* Fill in all details in the form and click 'Add Recipe'.
* Be redirected to the homepage.

Edit Recipe

* On 'My Recipes', click on 'Edit Recipe' when viewing a recipe card.
* Edit any details within the form.
* Click on 'Update Recipe' and be redirected to 'home.html'.

Delete Recipe

* On 'My Recipes', click on 'Delete Recipe' when viewing a recipe card.
* Be redirected to 'My Recipes' and see if the recipe has been deleted from the database.

Return To Homepage

* Click on 'Return To Homepage' and be redirected to 'home.html'.

Sign Out

* Click on Sign Out and be directed to the message page with options to sign back in or return to homepage.

### Responsiveness Testing ###
This application has been tested on all mobile, tablet and desktop screen sizes with the Google Chrome Developer Tools. From these tests, all issues have been resolved.

### Code Validation ###
The HTML, CSS and JavaScript code for this application has been run through and validated by The W3C Markup Validation Service and JSHint.

### Bugs ###
* main ingredient dropdown didn't work. Solved, tested and it worked. 
* in recipes by categories there were many komma's between the names. Had to make small adjustment to database in mongoDB. 
* category dropdown could not search for categories. Made a small adjustment to the particular database. Tested it and worked.
* in responsive mode, the hambo and the back-to-top btn didn't work. Had to add the jquery to every html page. Tested and it worked.
* the method and ingredients didn't work. Had to fill in the mongodb atlas database. Tested and it worked. 
* The live employment on Heroku didn't work. Forgot to enter the MONGO_URI in the config vars. Tested it and it worked.

## Deployment ##
The source code for this application can be found on Github and the application itself has been deployed onto Heroku. There is no difference between the GitHub code and the code in the live application.

It can be installed with the following steps:

* Download the git repository
* Sign up/login to Heroku.com
* From the dashboard click Create New App
* Enter a unique name and your region and click Create
* From your command line, enter heroku to ensure heroku is installed (if not installed this can be done with sudo snap install --classic heroku)
* heroku login

* Enter your credentials for heroku.com
sudo pip3 install Flask
sudo pip3 install pymongo
sudo pip3 freeze --local > requirements.txt
echo web: python run.py > Procfile
git add .
git commit -m "initial commit"
git push -u heroku master
heroku ps:scale web=1

* Make sure to set debug to True.

* From heroku.com app settings: set config vars to IP : 0.0.0.0, PORT : 5000 and MONGO_URI :mongodb+srv://[username]:[password]@myfirstdatabasecluster-8hied.mongodb.net/digital_kitchen?retryWrites=true, ensuring that you update the username and password accordingly.

* Click More > Restart all Dynos

* Application is live at https://your-app-name.herokuapp.com/

## Credits and Acknowledgements ##
I would like to credit Luigi van der Plas, the tutors and my mentor Chris Zielinski for helping me fix all of the minor bugs within the application, and I would also like to credit the Code Institute Data Centric Development lessons.

## Media ## 
All images used in this application are obtained from [BBC Goodfood](https://www.bbcgoodfood.com/ "BBC Goodfood").

## Important Note ##
The commits and pushes on GitHub needs some explaination. In the beginning i committed some steps and after i realized I didn't commit for a long time i pushed a huge amount of code. Then, because i am a junior and thought Google is your best friend, i wanted to delete the repo and start all over because i thought that would look nicer. 
I deleted my repo and made a new one. That's why it says 'Initial Commit' later then the odd commits, i didn't know that. I realize now that i can't make any commits without changes and push that commit to GitHub. 
Sorry for this and it won't happen in the future. It is a big lesson to always commit the steps. 