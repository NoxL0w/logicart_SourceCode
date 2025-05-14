from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from Logicart_BackEnd.databaseManagement import db_user
import random

app = Flask(__name__)

def sessionKey_Gen():
    sessionkey = random.randint(1000000000,9999999999)
    return sessionkey

app.secret_key = sessionKey_Gen()

@app.route('/homepage')
def dashboard():
    return render_template('Dashboard.html')

@app.route('/')
def home():
    return redirect(url_for("login"))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = db_user.authenticate_user(username, password)
        if user:
            session['user_id'] = user.id  # Store user ID in the session
            session['username'] = user.username  # Store username for profile
            return redirect(url_for("dashboard"))  # Redirect to dashboard or home
        return "Invalid credentials"
    return render_template('Dashboard.html')

@app.route("/register", methods=["POST"])
def register_route():
    data = request.form
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")
    first_name = data.get("first_name")
    last_name = data.get("last_name")

    success = db_user.register_user(username, password, email, first_name, last_name)
    if success:
        return redirect(url_for("login"))  # Redirect to login page after successful registration
    else:
        return "Registration failed", 400
    
@app.route('/logout')
def logout():
    session.clear()  # Clear the session to log the user out
    return redirect(url_for('home'))