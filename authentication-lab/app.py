from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

config = {
  "apiKey": "AIzaSyAWaRHUqwrmmoONZ-Epzhs5Upmj0mWukLY",
  "authDomain": "jan-proj.firebaseapp.com",
  "projectId": "jan-proj",
  "storageBucket": "jan-proj.appspot.com",
  "messagingSenderId": "855107059967",
  "appId": "1:855107059967:web:c834ccb37b723123328cca",
  "measurementId": "G-XE83F71KXG",
  'databaseURL': 'https://jan-proj-default-rtdb.europe-west1.firebasedatabase.app/'
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

@app.route('/', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
        except:
            return render_template("signin.html")

    return render_template("signin.html")



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
        except:
            return render_template("signup.html")

    return render_template("signup.html")



@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")

@app.route('/signout')
def signout():
    login_session['user'] = None
    auth.current_user = None
    return redirect(url_for('signin'))



if __name__ == '__main__':
    app.run(debug=True)