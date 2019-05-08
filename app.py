import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
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
    
    
  
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)