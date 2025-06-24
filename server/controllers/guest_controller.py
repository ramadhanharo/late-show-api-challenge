from flask import Blueprint, jsonify, abort
from server.models.guest import Guest

guest_bp = Blueprint('guest_bp', __name__, url_prefix='/guests')

@guest_bp.route('', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([g.to_dict() for g in guests]), 200

@guest_bp.route('/<int:id>', methods=['GET'])
def get_guest(id):
    guest = Guest.query.get(id)
    if not guest:
        abort(404, description="Guest not found")
    return jsonify(guest.to_dict_with_appearances()), 200
