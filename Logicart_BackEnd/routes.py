from flask import Flask, render_template, request, redirect, url_for, jsonify
from Logicart_BackEnd.databaseManagement import db_user

app = Flask(__name__)

@app.route('/homepage')
def dashboard():
    return render_template('HomePage.html')

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
            logStatus = True
            return redirect(url_for("dashboard"))  # Later redirect to dashboard
        return "Invalid credentials"
    return render_template('LoginForm.html')

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