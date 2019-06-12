import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.secret_key = 'some_secret'

app.config["MONGO_DBNAME"] = 'digital_kitchen'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

@app.route('/')

@app.route('/index')
def index():
    if 'username' in session:
        return render_template("index.html",
        recipes=mongo.db.recipes.find(),
        cuisines=mongo.db.cuisines.find(),
        categories=mongo.db.categories.find(),
        difficulties=mongo.db.difficulties.find(),
        main_ingredients=mongo.db.main_ingredients.find(),
        allergens=mongo.db.allergens.find(),
        message='Welcome, '+ str(session['username']) + ', to The Digital Kitchen!')
    return render_template("index.html", 
    message='Welcome to The Digital Kitchen!',
    recipes=mongo.db.recipes.find(),
    categories=mongo.db.categories.find(),
    difficulties=mongo.db.difficulties.find(),
    main_ingredients=mongo.db.main_ingredients.find(),
    allergens=mongo.db.allergens.find(),
    cuisines=mongo.db.cuisines.find())
    

@app.route('/all_recipes')
def all_recipes():
    """
    Display all recipes on one page
    """
    recipes = mongo.db.recipes.find()
    recipes_total = recipes.count()
    return render_template("allrecipes.html",
                            recipes_total=recipes_total,
                            recipes=recipes)

@app.route('/recipes_by_category/<category_name>')
def recipes_by_category(category_name):
    """
    Get all recipes of a chosen category and display
    these recipes on one page
    """
    # Counts total amount of chosen category recipes
    recipes_total = mongo.db.recipes.find({
        "category_name": category_name
    }).count()
    return render_template(
        "recipes_by_category.html",
        recipes=mongo.db.recipes.find({"category_name": category_name}),
        categories=mongo.db.categories.find(),
        category_name=category_name,
        recipes_total=recipes_total)


@app.route('/recipes_by_main/<main_ingredient>')
def recipes_by_main(main_ingredient):
    """
    Get all recipes of a chosen ingredient and display
    these recipes on one page
    """
    # Counts total amount of chosen ingredient recipes
    recipes_total = mongo.db.recipes.find({
        "main_ingredient": main_ingredient
    }).count()
    return render_template(
        "recipes_by_main.html",
        recipes=mongo.db.recipes.find({"main_ingredient": main_ingredient}),
        main_ingredients=mongo.db.main_ingredients.find(),
        main_ingredient=main_ingredient,
        recipes_total=recipes_total)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    """
    Direct user to signin page where they can enter their username
    and password and manage their recipes
    """
    if 'username' in session:
        return render_template('index.html',
            message="You are already signed in!")
    
    if request.method == 'POST':
        users = mongo.db.users
        user_signin = users.find_one({'username': request.form['username']})

        if user_signin:
            if request.form['password'] == user_signin['password']:
                session['username'] = request.form['username']
                return redirect(url_for('index'))
        return render_template('signin.html', 
                                message='Invalid username or password')
    return render_template('signin.html', message='')
    
    
@app.route('/signout')
def signout():
    """
    Sign user out of the session
    """
    if 'username' in session:
        session.pop('username')
        return render_template('message.html',
                               message='Signed out. See you later!')
    return render_template('message.html',
                            message='You have already signed out!')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Register new user into the database
    """
    if 'username' in session:
        return render_template('register.html', 
                        message='You are already signed in and registered')
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username' : request.form['username']})
        if request.form['username'] and request.form['password']:
            # Check for existing user to avoid re-registering the same user
            if existing_user is None:
                password = request.form['password']
                users.insert({'username': request.form['username'],
                              'password': password})
                session['username'] = request.form['username']
                return redirect(url_for('index'))
            return render_template('register.html',
            message='Username ' + str(existing_user['username']) + ' already exists')
        return render_template('register.html',
                                message='Enter a username and password')
    return render_template('register.html', message='')

@app.route('/get_recipe/<recipe_id>')
def get_recipe(recipe_id):
    """
    Get recipe and display it on getrecipe.html
    """
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    # Splits ingredients input into a list    
    ingredient_split = the_recipe['recipe_ingredients'].split('\n')
    for ingredient in ingredient_split:
        print(ingredient)
    # Splits methods input into a list    
    method_split = the_recipe['recipe_method'].split('\n')
    for method in method_split:
        print(method)
    return render_template("getrecipe.html",
                            recipe=the_recipe,
                            ingredient_split=ingredient_split,
                            method_split=method_split)

@app.route('/recipes_by_cuisine/<cuisine_name>')
def recipes_by_cuisine(cuisine_name):
    """
    Get all recipes of a chosen cuisine and display
    these recipes on one page
    """
    # Counts total amount of chosen cuisine recipes
    recipes_total = mongo.db.recipes.find({
        "cuisine_name": cuisine_name
    }).count()
    return render_template(
        "recipes_by_cuisine.html",
        recipes=mongo.db.recipes.find({"cuisine_name": cuisine_name}),
        cuisines=mongo.db.cuisines.find(),
        cuisine_name=cuisine_name,
        recipes_total=recipes_total)
        
@app.route('/<username>/add_recipe', methods=['GET','POST'])
def add_recipe(username):
    """
    If user is signed in, allow user to create and insert
    new recipe into the database
    """
    if 'username' in session:
        username = session['username']
        if request.method == 'POST':
            recipe = mongo.db.recipes
            recipe.insert({
                'recipe_name' : request.form['recipe_name'],
                'recipe_description' : request.form['recipe_description'],
                'cuisine_name' : request.form.get('cuisine_name'),
                'recipe_ingredients' :  request.form.get('recipe_ingredients'),
                'recipe_method' : request.form.get('recipe_method'),
                'cook_time': request.form.get('cook_time'),
                'image_url': request.form.get('image_url'),
                'author' : session['username'],
                'category_name': request.form.getlist('category_name'),
                'main_ingredient': request.form.get('main_ingredient')
            })
            # Check for existing ingredient to avoid 
            # re-entering the same ingredient into database
            # Adds new main ingredient into database if does not exist
            main_ingredient = mongo.db.main_ingredients
            existing_ingredient = main_ingredient.find_one({
                'main_ingredient' : request.form['main_ingredient']
            })
            if request.form['main_ingredient']:
                if existing_ingredient is None:
                    main_ingredient.insert({
                    'main_ingredient': request.form.get('main_ingredient')
                    })
                return redirect(url_for('index'))
        return render_template('addrecipe.html', 
                            cuisines=mongo.db.cuisines.find(),
                            difficulties=mongo.db.difficulties.find(),
                            categories=mongo.db.categories.find(),
                            main_ingredients=mongo.db.main_ingredients.find(),
                            allergens=mongo.db.allergens.find(),
                            username=session['username'])     
    return render_template('signin.html')


@app.route('/<username>/edit_recipe/<recipe_id>', methods=["GET",'POST'])
def edit_recipe(username, recipe_id):
    """
    Direct user to editrecipe.html and update chosen recipe
    once user presses 'update recipe' button
    """
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    cuisines = mongo.db.cuisines.find()
    difficulties = mongo.db.difficulties.find()
    if 'username' in session:
        return render_template('editrecipe.html',
                    recipe=the_recipe,
                    cuisines=cuisines,
                    difficulties=difficulties,
                    categories=mongo.db.categories.find(),
                    main_ingredients=mongo.db.main_ingredients.find(),
                    allergens=mongo.db.allergens.find(),
                    username=session['username'])
    return render_template('signin.html',
                    message='Please sign in or register to edit a recipe!')


@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    """
    Update the recipe in the database and direct user
    back to the recipe
    """
    if 'username' in session:
        recipes = mongo.db.recipes
        recipes.update(
                {'_id': ObjectId(recipe_id)},
                {
                    'recipe_name': request.form.get('recipe_name'),
                    'cuisine_name': request.form.get('cuisine_name'),
                    'recipe_ingredients': request.form.get('recipe_ingredients'),
                    'recipe_method': request.form.get('recipe_method'),
                    'cook_time': request.form.get('cook_time'),
                    'recipe_description': request.form.get('recipe_description'),
                    'image_url': request.form.get('image_url'),
                    'author': session['username'],
                    'category_name': request.form.getlist('category_name'),
                    'main_ingredient': request.form.get('main_ingredient')
                })
        return redirect(url_for('get_recipe', recipe_id=recipe_id,
                                        username=session['username']))


@app.route('/<username>/delete_recipe/<recipe_id>')
def delete_recipe(username, recipe_id):
    """
    Delete recipe from database
    """
    if 'username' in session:
        mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
        return redirect(url_for('my_recipes', username=session['username']))
    return render_template('signin.html',
                    message='Please sign in or register to delete a recipe!')


@app.route('/my_recipes/<username>')
def my_recipes(username):
    """
    Display all recipes created by user in session
    """
    if 'username' in session:
        user = mongo.db.users.find_one({"username": username})
        user_recipes = mongo.db.recipes.find({"author": session['username']})
        recipes_total = user_recipes.count()
        return render_template("myrecipes.html",
                                recipes_total=recipes_total,
                                user=user,
                                user_recipes=user_recipes,
                                message="Your Recipes",)
    else:
        return redirect(url_for('index',
                                message="You do not have any recipes!"))
    
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)