from ..database import DatabaseConnection


class Channel:
    """Channel model class"""

    def __init__(self, channel_id=None, name=None, server_id=None):
        """Constructor method"""
        self.channel_id = channel_id
        self.name = name
        self.server_id = server_id

    def serialize(self):
        """Serialize object representation"""
        return {
            "channel_id": self.channel_id,
            "name": self.name,
            "server_id": self.server_id
        }

    @classmethod
    def get(cls, channel):
        """Get a channel by ID"""
        query = """SELECT * FROM bk9kjvgo2gjf3qeyk1dt.Channels WHERE id = %s"""
        params = (channel.channel_id,)
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(*result)
        return None

    @classmethod
    def get_all(cls, server_id):
        """Get all channels in a server"""
        query = """SELECT * FROM bk9kjvgo2gjf3qeyk1dt.Channels WHERE server_id = %s"""
        params = (server_id,)
        results = DatabaseConnection.fetch_all(query, params=params)

        channels = []
        if results is not None:
            for result in results:
                channels.append(cls(*result))
            return channels

    @classmethod
    def create(cls, channel):
        """Create a new channel"""
        query = """INSERT INTO Channels (name, server_id) VALUES (%s, %s)"""
        params = (channel.name, channel.server_id)

        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete(cls, channel):
        """Delete a channel"""
        query = """DELETE FROM Channels WHERE id = %s"""
        params = (channel.channel_id,)

        DatabaseConnection.execute_query(query, params=params)
