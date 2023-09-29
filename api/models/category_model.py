from ..database import DatabaseConnection


class Category:
    def __init__(self, category_id=None, name=None, img=None):
        self.category_id = category_id
        self.name = name
        self.img = img

    def serialize(self):
        return {
            "category_id": self.category_id,
            "name": self.name
        }

    @classmethod
    def create(cls, category):
        query = "INSERT INTO categories (name) VALUES (%s)"
        params = (category.name,)

        cursor = DatabaseConnection.execute_query(query, params=params)
        category.category_id = cursor.lastrowid

    @classmethod
    def get_all(cls):
        query = """SELECT * FROM bk9kjvgo2gjf3qeyk1dt.Categories"""
        results = DatabaseConnection.fetch_all(query)
        categories = []
        if results is not None:
            for result in results:
                categories.append(cls(*result))
            return categories

    @classmethod
    def get(cls, category_id):
        query = "SELECT * FROM categories WHERE category_id = %s"
        params = (category_id,)

        category = DatabaseConnection.fetch_one(query, params=params)

        if category:
            return cls(category_id=category[0], name=category[1])
        else:
            return None

    @classmethod
    def update(cls, category):
        query = "UPDATE categories SET name = %s WHERE category_id = %s"
        params = (category.name, category.category_id)

        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete(cls, category_id):
        query = "DELETE FROM categories WHERE category_id = %s"
        params = (category_id,)

        DatabaseConnection.execute_query(query, params=params)
