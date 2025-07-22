from flask_sqlalchemy import SQLAlchemy

# This is an instance of SQLAlchemy, which will be initialised in the main app.py
db = SQLAlchemy()

class Workout(db.Model):
    """
    Represents a single workout entry in the database.
    This table will store the details of each exercise logged by the user.
    """
    id = db.Column(db.Integer, primary_key=True)
    exercise = db.Column(db.String(100), nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    sets = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        """
        Provides a developer-friendly string representation of the Workout object,
        useful for debugging.
        """
        return f'<Workout {self.id}: {self.exercise} - {self.reps} reps at {self.weight} kg for {self.sets} sets>'

