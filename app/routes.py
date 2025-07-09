from flask import Blueprint, request, jsonify
from app.models import Meal
from app.database import db
from datetime import datetime

bp = Blueprint('routes_bp', __name__)

@bp.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Daily Diet API rodando!"})

@bp.route('/meals', methods=['POST'])
def create_meal():
    data = request.json

    try:
        new_meal = Meal(
            name=data['name'],
            description=data.get('description', ''),
            date_time=datetime.strptime(data['date_time'], "%Y-%m-%d %H:%M"),
            is_on_diet=data['is_on_diet']
        )
        db.session.add(new_meal)
        db.session.commit()

        return jsonify({"message": "Refeição criada com sucesso!", "meal": new_meal.to_dict()}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400
