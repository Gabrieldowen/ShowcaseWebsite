# app.py
from flask import Flask
from routes.home import setup_routes

app = Flask(__name__, static_url_path='/static', static_folder='node_modules')
setup_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
