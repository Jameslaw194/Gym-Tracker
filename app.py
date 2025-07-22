from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

# Get the absolute path of the directory where the script is located
basedir = os.path.abspath(os.path.dirname(__file__))

# --- Flask App Initialisation ---
app = Flask(__name__)
# --- Database Configuration ---
# Use the absolute path to ensure the database file is found correctly
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'workouts.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- Routes ---
@app.route('/')
def index():

@app.route('/add', methods=['POST'])
def add_workout():

@app.route('/delete/<int:id>')
def delete_workout(id):

# --- Main Flask Execution ---
if __name__ == '__main__':
    # Create the database and tables if they don't exist
    with app.app_context():
        db.create_all()
    # Run the Flask application
    app.run(debug=True)
