from flask import request, jsonify
from ..models.role_permission_model import Role, Permission


class RolePermissionController:
    """Role and Permission controller class"""

    @classmethod
    def create_role(cls):
        data = request.json
        role = Role(name=data.get('name'))

        Role.create(role)
        return {'message': 'Role created successfully'}, 201

    @classmethod
    def create_permission(cls):
        data = request.json
        permission = Permission(name=data.get('name'))

        Permission.create(permission)
        return {'message': 'Permission created successfully'}, 201

    @classmethod
    def get_role(cls, role_id):
        role = Role.get(role_id)
        if role is not None:
            return role.serialize(), 200
        return {'message': 'Role not found'}, 404

    @classmethod
    def get_permission(cls, permission_id):
        permission = Permission.get(permission_id)
        if permission is not None:
            return permission.serialize(), 200
        return {'message': 'Permission not found'}, 404
