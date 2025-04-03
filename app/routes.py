from flask import Blueprint, jsonify

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return jsonify({"message": "Welcome to Flask GitHub Actions Demo!"})

@bp.route('/health')
def health_check():
    return jsonify({"status": "OK"})