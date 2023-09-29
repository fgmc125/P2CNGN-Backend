from ..database import DatabaseConnection
from flask import jsonify


class Member:
    """Member model class"""

    def __init__(self, member_id=None, user_id=None, server_id=None):
        """Constructor method"""
        self.member_id = member_id
        self.user_id = user_id
        self.server_id = server_id

    def serialize(self):
        """Serialize object representation"""
        return {
            "member_id": self.member_id,
            "user_id": self.user_id,
            "server_id": self.server_id
        }

    @classmethod
    def get(cls, member):
        """Get a member by ID"""
        query = """SELECT * FROM bk9kjvgo2gjf3qeyk1dt.Members WHERE id = %s"""
        params = (member.member_id,)
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(*result)
        return None

    @classmethod
    def get_all(cls):
        """Get all members in a server"""
        query = """SELECT * FROM bk9kjvgo2gjf3qeyk1dt.Members"""
        
        results = DatabaseConnection.fetch_all(query)

        members = []
        if results is not None:
            for result in results:
                members.append(cls(*result))
            return members

    @classmethod
    def create(cls, member):
        """Create a new member"""
        query = """INSERT INTO Members (user_id, server_id) VALUES (%s, %s)"""
        params = (member.user_id, member.server_id)

        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete(cls, member):
        """Delete a member"""
        query = """DELETE FROM Members WHERE id = %s"""
        params = (member.member_id,)

        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def get_member_user(cls,user):
        """Get all members in a server"""
        query = """SELECT Members.server_id, Servers.name 
        from bk9kjvgo2gjf3qeyk1dt.Members 
        join bk9kjvgo2gjf3qeyk1dt.Servers on Members.server_id = Servers.id
        WHERE Members.user_id = %s"""
        params = (user),
        
        results = DatabaseConnection.fetch_all(query,params=params)

        members = []
        if results is not None:
            for result in results:
                members.append(cls(*result))
            return members    