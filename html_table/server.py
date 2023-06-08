from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def render_table():
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'Kathleen', 'last_name' : 'Kavanagh'},
        {'first_name' : 'Nicholas', 'last_name' : 'Bowman'},
        {'first_name' : 'Dennis', 'last_name' : 'Kavanagh'},
        {'first_name' : 'Malcolm', 'last_name' : 'Bowman'}
    ]
    return render_template("table.html", user_info = users)



if __name__=="__main__":
    app.run(debug=True)