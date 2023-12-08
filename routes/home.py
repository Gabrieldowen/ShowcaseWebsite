# routes/main_routes.py
from flask import render_template

def setup_routes(app):
    @app.route('/')
    def home():
        return render_template('index.html')
