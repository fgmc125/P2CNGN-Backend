from ..database import DatabaseConnection


class Server:
    "User model class"""

    def __init__(self, server_id=None, name=None, description=None, img=None, user_id=None, category_id=None):
        """Constructor method"""
        self.server_id = server_id
        self.name = name
        self.description = description
        self.img = img
        self.user_id = user_id
        self.category_id = category_id

    def serialize(self):
        """Serialize object representation
        Returns:
            dict: Object representation
        """
        return {
            "server_id": self.server_id,
            "name": self.name,
            "description": self.description,
            "img": self.img,
            "user_id": self.user_id,
            "category_id": self.category_id
        }

    @classmethod
    def get(cls, server):
        """Get a server by id
        Args:
            - server (Server): Server object with the id attribute
        Returns:
            - Server: Server object
        """
        query = """SELECT * FROM bk9kjvgo2gjf3qeyk1dt.Servers 
        WHERE id = %s"""
        params = (server.server_id,)
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(*result)
        return None

    @classmethod
    def get_all(cls):
        """Get all servers
        Returns:
            - list: List of Server objects
        """
        query = """SELECT * FROM bk9kjvgo2gjf3qeyk1dt.Servers"""
        results = DatabaseConnection.fetch_all(query)

        servers = []
        if results is not None:
            for result in results:
                servers.append(cls(*result))
            return servers

    @classmethod
    def create(cls, server):
        """Create a new server
        Args:
            - server (Server): Server object
        """
        query = """INSERT INTO bk9kjvgo2gjf3qeyk1dt.Servers (name, description, img, user_id, category_id)
        VALUES (%s, %s, %s, %s, %s)"""
        params = server.name, server.description, server.img, server.user_id, server.category_id

        DatabaseConnection.execute_query(query, params=params)


    @classmethod
    def get_all_server(cls,user_id):
            """Get all servers
            Returns:
                - list: List of Server objects
            """
            query = """SELECT * FROM bk9kjvgo2gjf3qeyk1dt.Servers WHERE user_id = %s"""
            params = (user_id,)
            results = DatabaseConnection.fetch_all(query, params=params)
            print(results)
            servers = []
            if results is not None:
                for result in results:
                    servers.append(cls(*result))
                return servers
            
            
