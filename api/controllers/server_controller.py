from ..models.server_model import Server
from flask import request, session

from ..models.user_model import User


class ServerController:
    """Server controller class"""

    @classmethod
    def get(cls, server_id):
        """Get a server by id"""
        server = Server(server_id=server_id)

        result = Server.get(server)
        if result is not None:
            return result.serialize(), 200

    @classmethod
    def get_all(cls):
        """Get all servers"""
        server_objects = Server.get_all()
        
        servers = []
        for server in server_objects:
            servers.append(server.serialize())
        print(servers)
        return servers, 200

    @classmethod
    def create(cls):
        """Create a new server"""
        username = session.get('username')
        if username is None:
            return {"message": "Usuario no logueado"}, 401

        user = User.get(User(username=username))

        if user is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            data = request.json
            server = Server(user_id=user.user_id, **data)
            print(server.serialize())
            Server.create(server)
            return {'message': 'Server created successfully'}, 201

    @classmethod
    def get_all_server(cls, user_id):
        """Get all servers for a user
        Returns:
            - list: List of Users objects
        """

        server_objects = Server.get_all_server(user_id)
        servers = []
        for server in server_objects:
            servers.append(server.serialize())
        return servers, 200
