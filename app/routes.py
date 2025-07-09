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

@bp.route('/meals/<int:meal_id>', methods=['PUT'])
def update_meal(meal_id):
    data = request.get_json()
    meal = Meal.query.get_or_404(meal_id)

    try:
        meal.name = data.get('name', meal.name)
        meal.description = data.get('description', meal.description)
        meal.date_time = datetime.strptime(data.get('date_time', meal.date_time.strftime("%Y-%m-%d %H:%M")), "%Y-%m-%d %H:%M")
        meal.is_on_diet = data.get('is_on_diet', meal.is_on_diet)

        db.session.commit()
        return jsonify({"message": "Refeição atualizada com sucesso!", "meal": meal.to_dict()}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@bp.route('/meals/<int:meal_id>', methods=['DELETE'])
def delete_meal(meal_id):
    meal = Meal.query.get_or_404(meal_id)

    try:
        db.session.delete(meal)
        db.session.commit()
        return jsonify({"message": "Refeição excluída com sucesso!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400
