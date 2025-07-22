from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

# Get the absolute path of the directory where the script is located.
basedir = os.path.abspath(os.path.dirname(__file__))

# --- Flask App Initialisation ---
app = Flask(__name__)
# --- Database Configuration ---
# Use the absolute path to ensure the database file is found correctly.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'workouts.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Workout(db.Model):
    """Represents a single workout entry in the database."""
    id = db.Column(db.Integer, primary_key=True)
    exercise = db.Column(db.String(100), nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    sets = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Workout {self.exercise}>'


# --- Routes ---
@app.route('/')
def index():
    # Render the home page with a list of all workouts.
    workouts = Workout.query.all()
    return render_template('index.html', workouts=workouts)

@app.route('/add', methods=['POST'])
def add_workout():




    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_workout(id):



    return redirect(url_for('index'))

# --- Main Flask Execution ---
if __name__ == '__main__':
    # Create the database and tables if they don't exist.
    with app.app_context():
        db.create_all()
    # Run the Flask application.
    app.run(debug=True)
