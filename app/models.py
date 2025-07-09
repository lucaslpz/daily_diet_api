from datetime import datetime
from .database import db

class Meal(db.Model):
    __tablename__ = 'meals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date_time = db.Column(db.DateTime, default=datetime.utcnow)
    is_on_diet = db.Column(db.Boolean, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "date_time": self.date_time.strftime("%Y-%m-%d %H:%M"),
            "is_on_diet": self.is_on_diet
        }
