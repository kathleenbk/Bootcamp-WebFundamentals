from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'secret' # set a secret key for security purposes


@app.route('/')
def visits():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1
    return render_template("index.html")



# clearing out session
@app.route("/destroy_session")
def destroy_session():
    session.pop('visits')
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)

