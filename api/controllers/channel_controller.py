from flask import request, jsonify
from ..models.channel_model import Channel


class ChannelController:
    """Channel controller class"""

    @classmethod
    def create(cls, server_id):
        """Create a new channel in a server"""
        data = request.json
        channel = Channel(name=data.get('name'), server_id=server_id)

        Channel.create(channel)
        return {'message': 'Channel created successfully'}, 201

    @classmethod
    def get(cls, channel_id):
        """Get channel details by ID"""
        channel = Channel(channel_id=channel_id)

        result = Channel.get(channel)
        if result is not None:
            return result.serialize(), 200

    @classmethod
    def get_all(cls, server_id):
        """Get all channels in a server"""
        channel_objects = Channel.get_all(server_id)
        channels = []
        for channel in channel_objects:
            channels.append(channel.serialize())
        return channels, 200

    @classmethod
    def delete(cls, channel_id):
        """Delete a channel by ID"""
        channel = Channel(channel_id=channel_id)

        Channel.delete(channel)
        return {'message': 'Channel deleted successfully'}, 200
