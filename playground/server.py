from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def default():
    return 'play the game!'

@app.route('/play')
def play1():
    return render_template("index.html", num=3, color=blue)

@app.route('/play/<int:num>')
def lvl2(num):
    return render_template("index.html", num=num, color = blue)

@app.route('/play/<int:num>/<string:color>')
def lvl3(num, color):
    return render_template("index.html", num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)