from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User

@app.route("/")
def index():
    return redirect('/users')

@app.route("/users")
def users():
    users = User.get_all()
    return render_template("read.html", users=users)


@app.route("/user/new")
def new():
    return render_template("create.html")

@app.route('/user/create', methods=["POST"])
def create_user():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

@app.route('/user/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit.html",user=User.get_one(data))

@app.route('/user/update', methods=["POST"])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/destroy/<int:id>')
def destroy(id):
    data ={
        "id":id
    }
    User.destroy(data)
    return redirect('/users')

@app.route('/user/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("show.html",user=User.get_one(data))