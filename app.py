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
    
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)