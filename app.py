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
def get_index():
    return render_template("index.html", 
    message='Welcome to The Digital Kitchen!',
    recipes=mongo.db.recipes.find(),
    categories=mongo.db.categories.find(),
    main_ingredients=mongo.db.main_ingredients.find(),
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

  
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)