from flask import Blueprint
from ..controllers.role_permission_controller import RolePermissionController

role_permission_bp = Blueprint('role_permission_bp', __name__)

role_permission_bp.route('/role', methods=['POST'])(RolePermissionController.create_role)
role_permission_bp.route('/permission', methods=['POST'])(RolePermissionController.create_permission)
role_permission_bp.route('/role/<int:role_id>', methods=['GET'])(RolePermissionController.get_role)
role_permission_bp.route('/permission/<int:permission_id>', methods=['GET'])(RolePermissionController.get_permission)
