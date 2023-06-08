from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

# New recipe page
@app.route('/recipes/new')
def new_recipe():
    return render_template('newrecipe.html')


# Create new recipe
@app.route('/recipes/create', methods=["POST"])
def create_recipe():
    # Validate recipe
    is_valid = Recipe.validate_recipe(request.form)
    if not is_valid:
        return redirect('/recipes/new')

    # If recipe is valid, save
    data = {
        'name':request.form['name'],
        'description':request.form['description'],
        'directions':request.form['directions'],
        'time':request.form['time'],
        'date':request.form['date'],
        'user_id':session['user_id']
    }
    Recipe.save_recipe(data)
    return redirect('/dashboard')

@app.route('/recipes/<int:id>')
def show_recipe(id):
    if 'user_id' in session:
        user=User.get_one({'id':session['user_id']})
        data = {
        "id": id
        }
    
        return render_template("recipe.html", user=user, recipe=Recipe.get_one_recipe(data))
    if not 'user_id' in session:
        return render_template("dashboard.html")

@app.route('/recipes/destroy/<int:id>')
def destroy(id):
    data ={
        "id":id
    }
    Recipe.destroy(data)
    return redirect('/dashboard')

@app.route('/recipes/edit/<int:id>')
def edit(id):
    if 'user_id' in session:
        user=User.get_one({'id':session['user_id']})
        data = {
        "id": id
        }
    
        return render_template("editrecipe.html", user=user, recipe=Recipe.get_one_recipe(data))
    if not 'user_id' in session:
        return render_template("dashboard.html")


@app.route('/recipes/update/<int:id>', methods=["POST"])
def update(id):
    
    # Validate recipe
    is_valid = Recipe.validate_recipe(request.form)
    if not is_valid:
        return redirect(f'/recipes/edit/{id}')

    # If recipe is valid, save
    data = {
        'id': id,
        'name':request.form['name'],
        'description':request.form['description'],
        'directions':request.form['directions'],
        'time':request.form['time'],
        'date':request.form['date'],
        'user_id':session['user_id']
    }
    Recipe.update(data)
    return redirect('/dashboard')