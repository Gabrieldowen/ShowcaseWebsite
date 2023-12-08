# app.py
from flask import Flask
from routes.route import setup_routes

app = Flask(__name__, static_url_path='/static')
setup_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
