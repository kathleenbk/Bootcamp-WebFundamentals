from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash

database='recipes_schema'
class Recipe:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.description = db_data['description']
        self.directions = db_data['directions']
        self.time = db_data['time']
        self.date= db_data['date']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.user_id = db_data['user_id']

    @classmethod
    def save_recipe(cls, data):
        query  = "INSERT INTO recipes (name, description, directions, time, date, user_id) VALUES ( %(name)s, %(description)s, %(directions)s, %(time)s, %(date)s, %(user_id)s);"
        return connectToMySQL(database).query_db( query, data )

    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(database).query_db( query )
        recipes = []
        for recipe in results:
            recipes.append( cls(recipe) )
        return recipes

    @classmethod
    def get_one_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        result = connectToMySQL('recipes_schema').query_db(query, data)
        if result:
            return cls(result[0])
        return False

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL('recipes_schema').query_db(query, data)

    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, time=%(time)s, directions=%(directions)s, date=%(date)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('recipes_schema').query_db(query, data)

    # Recipe validation
    @staticmethod
    def validate_recipe( recipe ):
        is_valid = True
        if len(recipe['name'])< 3:
            is_valid = False
            flash("Name must be at least three characters.","recipe")
        if len(recipe['description'])< 3:
            is_valid = False
            flash("Description must be at least three characters.","recipe")
        if len(recipe['directions'])< 3:
            flash("Instructions must be at least three characters.","recipe")
            is_valid = False
        if recipe['date'] =='':
            flash("Must select a date.", "recipe")
            is_valid = False
        if 'time' not in recipe:
            flash("Must select if recipe is under thirty minutes.", "recipe")
            is_valid = False
        return is_valid
