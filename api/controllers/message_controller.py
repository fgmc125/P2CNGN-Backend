from flask import request, jsonify
from ..models.message_model import Message


class MessageController:
    """Message controller class"""

    @classmethod
    def send_message(cls, channel_id):
        """Send a message in a channel"""
        data = request.json
        message = Message(content=data.get('content'), id_channels=channel_id, users_id=data.get('users_id'))

        Message.send(message)
        return {'message': 'Message sent successfully'}, 201
    
    

    @classmethod
    def get(cls, message_id):
        """Get message details by ID"""
        message = Message(message_id=message_id)

        result = Message.get(message)
        if result is not None:
            return result.serialize(), 200

    @classmethod
    def get_messages_in_channel(cls, channel_id):
        """Get all messages in a channel"""
        message_objects = Message.get_messages_in_channel(channel_id)
        messages = []
        for message in message_objects:
            messages.append(message.serialize())
        return messages, 200

    @classmethod
    def delete(cls, message_id):
        """Delete a message by ID"""
        message = Message(message_id=message_id)

        Message.delete(message)
        return {'message': 'Message deleted successfully'}, 200
