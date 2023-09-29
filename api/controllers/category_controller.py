from flask import request, jsonify, session
from ..models.category_model import Category

class CategoryController:
    @classmethod
    def create_category(cls):
        if 'username' not in session:
            return {'message': 'Usuario no logueado'}, 401

        data = request.json
        category = Category(name=data.get('name'))
        Category.create(category)

        return {'message': 'Categoría creada correctamente', 'category_id': category.category_id}, 201

    @classmethod
    def get_all(cls):
        username = session.get('username')
        if username is None:
            return {"message": "Usuario no logueado"}, 401

        categories = Category.get_all()
        if len(categories) > 0:
            return jsonify(
                [{'category_id': category.category_id, 'name': category.name} for category in categories]
            ), 200
        else:
            return {'message': 'No se han encontrado categorias'}, 404

    @classmethod
    def get_category(cls, category_id):
        category = Category.get(category_id)
        if category:
            return {'category_id': category.category_id, 'name': category.name}, 200
        else:
            return {'message': 'Categoría no encontrada'}, 404

    @classmethod
    def update_category(cls, category_id):
        if 'username' not in session:
            return {'message': 'Usuario no logueado'}, 401

        data = request.json
        category = Category(category_id=category_id, name=data.get('name'))
        Category.update(category)

        return {'message': 'Categoría actualizada correctamente'}, 200

    @classmethod
    def delete_category(cls, category_id):
        if 'username' not in session:
            return {'message': 'Usuario no logueado'}, 401

        Category.delete(category_id)
        return {'message': 'Categoría eliminada correctamente'}, 200
