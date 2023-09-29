from ..models.user_model import User

from flask import request,session
from .validators import validate_user_data, validate_unique_email,validate_unique_username
from ..models.exceptions import InvalidDataError


class UserController:
    """User controller class"""

    @classmethod
    def login(cls):
        data = request.json
        user = User(
            username=data.get('username'),
            password=data.get('password')
        )

        if User.is_registered(user):
            session['username'] = data.get('username')
            return {"message": "Sesion iniciada"}, 200
        else:
            return {"message": "Usuario o contraseña incorrectos"}, 401

    @classmethod
    def show_profile(cls):
        username = session.get('username')

        if username is None:
            return {"message": "Usuario no logueado"}, 401

        user = User.get(User(username=username))
        if user is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            return user.serialize(), 200

    @classmethod
    def logout(cls):
        session.pop('username', None)
        return {"message": "Sesion cerrada"}, 200

    @classmethod
    def create(cls):
        """Create a new user"""
        data = request.json

        #validate data
        data = validate_user_data(data)
        
        if not validate_unique_username(data['username']):
            raise InvalidDataError('El nombre de usuario ya existe')
        
        if 'email' not in data or data['email'] is None:
            raise InvalidDataError('El correo electrónico es obligatorio')
        
        if not validate_unique_email(data['email']):
            raise InvalidDataError('El correo electrónico ya existe')
        
        #create user
        user = User(**data)

        User.create(user)
        return {'message': 'User created successfully'}, 201
      
    @classmethod
    def update(cls, user_id):
        """Update a film"""
        data = request.json

         #validate data a verificar si funciona
        data = validate_user_data(data)
        """
        if not validate_unique_username(data['username'], user_id):
            raise InvalidDataError('El nombre de usuario ya existe')
        """
        """
        if not validate_unique_email(data['email'], user_id):
            raise InvalidDataError('El correo electrónico ya existe')
        """
        

        data['user_id'] = user_id

        user = User(**data)
        User.update(user)
        
        return {'message': 'User updated successfully'}, 

    @classmethod
    def get_all(cls):
        """Get all servers"""
        user_objects = User.get_all()
        users = []
        for user in user_objects:
            users.append(user.serialize())
        return users, 200
        
    @classmethod
    def get_user(cls, user_id):
        """Get a user by id"""
        user = User(user_id=user_id)
        result = User.get_user(user)
        if result is not None:
            return result.serialize(), 200
        
    @classmethod
    def get_all_user(cls, user_id):
        """Get all servers for a user
        Returns:
            - list: List of Users objects
        """
        user_objects = User.get_all_user(user_id)
        users = []
        for user in user_objects:
            users.append(user.serialize())
        return users, 200
        
        

