from flask import Blueprint, request, jsonify
from ..controllers.member_controller import MemberController

member_bp = Blueprint('member_bp', __name__)

# Rutas relacionadas con los canales
member_bp.route('/<int:member_id>', methods=['GET'])(MemberController.get)
member_bp.route('/create', methods=['POST'])(MemberController.create)
member_bp.route('/<int:member_id>', methods=['DELETE'])(MemberController.delete)

member_bp.route('/', methods=['GET'])(MemberController.get_all)
member_bp.route('/user/<int:user_id>', methods=['GET'])(MemberController.get_member_user)
