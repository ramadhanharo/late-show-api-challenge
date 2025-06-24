from flask import Blueprint, jsonify, abort
from server.models.episode import Episode

episode_bp = Blueprint('episode_bp', __name__, url_prefix='/episodes')

@episode_bp.route('', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([e.to_dict() for e in episodes]), 200

@episode_bp.route('/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        abort(404, description="Episode not found")
    return jsonify(episode.to_dict_with_appearances()), 200
