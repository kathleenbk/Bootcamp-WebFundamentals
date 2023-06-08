from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html", num = 4)

@app.route('/<int:num>')
def rows(num):
    return render_template("index.html", num = num, num2=8)

@app.route('/<int:num>/<int:num2>')
def columnsandrows(num, num2):
    return render_template("index.html", num = num, num2=num2) 

if __name__=="__main__":
    app.run(debug=True)