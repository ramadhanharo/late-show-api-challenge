from flask import Blueprint, request, jsonify, abort
from server.models.appearance import Appearance
from server.models.guest import Guest
from server.models.episode import Episode
from server.models import db

appearance_bp = Blueprint('appearance_bp', __name__, url_prefix='/appearances')


# POST /appearances
@appearance_bp.route('', methods=['POST'])
def create_appearance():
    data = request.get_json()

    episode_id = data.get("episode_id")
    guest_id = data.get("guest_id")
    rating = data.get("rating")

    if not all([episode_id, guest_id, rating]):
        abort(400, description="Missing required fields.")

    appearance = Appearance(
        episode_id=episode_id,
        guest_id=guest_id,
        rating=rating
    )

    db.session.add(appearance)
    db.session.commit()

    return jsonify(appearance.to_dict_with_guest()), 201


# DELETE /appearances/<id>
@appearance_bp.route('/<int:id>', methods=['DELETE'])
def delete_appearance(id):
    appearance = Appearance.query.get(id)

    if not appearance:
        return jsonify({"error": "Appearance not found"}), 404

    db.session.delete(appearance)
    db.session.commit()

    return jsonify({"message": "Appearance successfully deleted"}), 200
