from app.database import db
from datetime import datetime

class Meal(db.Model):  # <-- aqui está certo
    __tablename__ = 'meals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date_time = db.Column(db.DateTime, default=datetime.utcnow)
    is_on_diet = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "date_time": self.date_time.strftime("%Y-%m-%d %H:%M"),
            "is_on_diet": self.is_on_diet,
            "user_id": self.user_id
        }
