from flask import request, jsonify, render_template, redirect, url_for
from .databaseManagement import db_user

def register_routes(app):
    @app.route('/')
    def home():
        return render_template('LoginForm.html')  # Login page

    @app.route('/login', methods=['POST'])
    def login():
        user_id = request.form.get('UserID')
        password = request.form.get('Password')

        user = db_user.get_user_by_id(user_id)

        if user and user['Password'] == password:
            return f"Welcome, {user['FirstName']} {user['LastName']}!"
        else:
            return "Invalid credentials", 401

    @app.route('/register', methods=['POST'])
    def register():
        data = request.form  # from HTML form
        try:
            db_user.register_user({
                'UserID': data['UserID'],
                'Username': data['Username'],
                'Password': data['Password'],
                'AccountType': data.get('AccountType', 'Individual'),
                'Email': data['Email'],
                'ContactNum': data['ContactNum'],
                'TelephoneNum': data['TelephoneNum'],
                'FirstName': data['FirstName'],
                'LastName': data['LastName'],
                'CompanyName': data.get('CompanyName', ''),
                'Owner': data.get('Owner', '')
            })
            return redirect(url_for('home'))
        except Exception as e:
            return f"Error: {e}", 500
