from flask import Blueprint
from ..controllers.category_controller import CategoryController

category_bp = Blueprint('category_bp', __name__)

category_bp.route('/categories', methods=['POST'])(CategoryController.create_category)
category_bp.route('/categories', methods=['GET'])(CategoryController.get_all)
category_bp.route('/categories/<int:category_id>', methods=['GET'])(CategoryController.get_category)
category_bp.route('/categories/<int:category_id>', methods=['PUT'])(CategoryController.update_category)
category_bp.route('/categories/<int:category_id>', methods=['DELETE'])(CategoryController.delete_category)
