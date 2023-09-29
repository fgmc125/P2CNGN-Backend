from ..database import DatabaseConnection


class Message:
    """Message model class"""

    def __init__(self, message_id=None, users_id=None, id_channels=None, content=None, created=None, username=None):
        """Constructor method"""
        self.username = username

        self.message_id = message_id
        self.users_id = users_id
        self.id_channels = id_channels
        self.content = content
        self.created = created

    def serialize(self):
        """Serialize object representation"""
        return {
            "username": self.username,
            "message_id": self.message_id,
            "id_users": self.users_id,
            "id_channels": self.id_channels,
            "content": self.content,
            "created": self.created
        }

    @classmethod
    def send(cls, message):
        """Send a message"""
        query = """INSERT INTO bk9kjvgo2gjf3qeyk1dt.Messages (id_users, id_channels, content) VALUES (%s, %s, %s)"""
        params = (message.users_id, message.id_channels, message.content)

        DatabaseConnection.execute_query(query, params=params)

        
|

    @classmethod
    def get(cls, message):
        """Get message details by ID"""
        query = """SELECT * FROM bk9kjvgo2gjf3qeyk1dt.Messages WHERE id = %s"""
        params = (message.message_id,)
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(*result)
        return None

    @classmethod
    def get_messages_in_channel(cls, channel_id):
        """Get all messages in a channel"""
        #query = """SELECT * FROM bk9kjvgo2gjf3qeyk1dt.Messages WHERE id_channels = %s"""
        query = """
        SELECT Users.id, Users.username, Messages.id, Messages.content, Messages.created
        FROM bk9kjvgo2gjf3qeyk1dt.Messages
        JOIN bk9kjvgo2gjf3qeyk1dt.Users ON Messages.id_users = Users.id
        WHERE Messages.id_users = Users.id AND Messages.id_channels = %s;
        """

        params = (channel_id,)
        results = DatabaseConnection.fetch_all(query, params=params)

        messages = []
        if results is not None:
            for result in results:
                messages.append(cls(*result))
            return messages


        # messages = []
        #
        # if results is not None:
        #     for result in results:
        #         user_id, username, message_id, content, created = result
        #         json_result = {
        #             'Users.id': user_id,
        #             'Users.username': username,
        #             'Messages.id': message_id,
        #             'Messages.content': content,
        #             'Messages.created': created
        #         }
        #         messages.append(json_result)
        #     return messages

    @classmethod
    def delete(cls, message):
        """Delete a message by ID"""
        query = """DELETE FROM Messages WHERE id = %s"""
        params = (message.message_id,)

        DatabaseConnection.execute_query(query, params=params)
