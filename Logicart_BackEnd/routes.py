from flask import Flask, render_template, request, redirect, url_for
from Logicart_BackEnd.databaseManagement import db_user

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = db_user.authenticate_user(username, password)
        if user:
            return "Login successful!"  # Later redirect to dashboard
        return "Invalid credentials"
    return render_template('LoginForm.html')
