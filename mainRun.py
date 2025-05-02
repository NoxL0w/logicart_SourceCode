from flask import Flask
from Logicart_BackEnd.routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    register_routes(app)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
