from ..database import DatabaseConnection


class Role:
    """Role model class"""

    def __init__(self, role_id=None, name=None):
        self.role_id = role_id
        self.name = name

    def serialize(self):
        return {
            "role_id": self.role_id,
            "name": self.name
        }

    @classmethod
    def create(cls, role):
        query = "INSERT INTO Roles (name) VALUES (%s)"
        params = (role.name,)

        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def get(cls, role_id):
        query = "SELECT * FROM Roles WHERE role_id = %s"
        params = (role_id,)
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(*result)
        return None


class Permission:
    """Permission model class"""

    def __init__(self, permission_id=None, name=None):
        self.permission_id = permission_id
        self.name = name

    def serialize(self):
        return {
            "permission_id": self.permission_id,
            "name": self.name
        }

    @classmethod
    def create(cls, permission):
        query = "INSERT INTO Permissions (name) VALUES (%s)"
        params = (permission.name,)

        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def get(cls, permission_id):
        query = "SELECT * FROM Permissions WHERE permission_id = %s"
        params = (permission_id,)
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(*result)
        return None
