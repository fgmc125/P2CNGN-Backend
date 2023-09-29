from flask import Blueprint, request, jsonify
from ..controllers.message_controller import MessageController

message_bp = Blueprint('message_bp', __name__)

# Rutas relacionadas con los mensajes
message_bp.route('/<int:message_id>', methods=['GET'])(MessageController.get)
message_bp.route('/send/<int:channel_id>', methods=['POST'])(MessageController.send_message)
message_bp.route('/channel/<int:channel_id>', methods=['GET'])(MessageController.get_messages_in_channel)
message_bp.route('/<int:message_id>', methods=['DELETE'])(MessageController.delete)
