from ..database import DatabaseConnection


class User:
    "User model class"""

    def __init__(self, user_id=None, username=None, password=None,
                 email=None, img=None):
        """Constructor method"""
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.img = img

    def serialize(self):
        """Serialize object representation
        Returns:
            dict: Object representation
        """
        return {
            "user_id": self.user_id,
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "img": self.img
        }

    @classmethod
    def is_registered(cls, user):
        query = """SELECT id FROM bk9kjvgo2gjf3qeyk1dt.Users 
        WHERE username = %(username)s and password = %(password)s"""
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return True
        return False

    @classmethod
    def get(cls, user):
        query = """SELECT * FROM bk9kjvgo2gjf3qeyk1dt.Users 
        WHERE username = %(username)s"""
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(
                user_id=result[0],
                username=result[1],
                password=result[2],
                email=result[3],
                img=result[4]
            )
        return None

    @classmethod
    def create(cls, user):
        """Create a new user
        Args:
            - user (User): User object
        """
        query = """INSERT INTO bk9kjvgo2gjf3qeyk1dt.Users (username, password, email, img)
        VALUES (%s, %s, %s, %s)"""
        params = user.username, user.password, user.email, user.img

        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update(cls, user):
        """Update a user
        Args:
            - user (User): User object
        """

        allowed_columns = {'username', 'password', 'email', 'img'}

        query_parts = []
        params = []
        for key, value in user.__dict__.items():
            if key in allowed_columns and value is not None:
                # value = ','.join(value)

                query_parts.append(f"{key} = %s")
                params.append(value)

        params.append(user.user_id)

        query = "UPDATE bk9kjvgo2gjf3qeyk1dt.Users SET " + ", ".join(query_parts) + " WHERE id = %s"
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def get_all(cls):
        """Get all Users
        Returns:
            - list: List of User objects
        """
        query = """SELECT * FROM bk9kjvgo2gjf3qeyk1dt.Users"""
        results = DatabaseConnection.fetch_all(query)

        users = []
        if results is not None:
            for result in results:
                users.append(cls(*result))
            return users

    @classmethod
    def get_user(cls, user):
        """Get a user by id
        Args:
            - user (User): Server object with the id attribute
        Returns:
            - User: User object
        """
        query = """SELECT * FROM bk9kjvgo2gjf3qeyk1dt.Users 
        WHERE id = %s"""
        params = (user.user_id,)
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(*result)
        return None

    @classmethod
    def get_all_user(cls,user_id):
        """Get all servers
        Returns:
            - list: List of Server objects
        """
        query = """SELECT * FROM bk9kjvgo2gjf3qeyk1dt.Users where Users.id = %s"""
        params = (user_id,)
        results = DatabaseConnection.fetch_all(query, params=params)


        users = []
        if results is not None:
            for result in results:
                users.append(cls(*result))
            return users