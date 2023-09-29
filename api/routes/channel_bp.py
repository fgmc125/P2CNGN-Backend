from flask import Blueprint, request, jsonify
from ..controllers.channel_controller import ChannelController

channel_bp = Blueprint('channel_bp', __name__)

# Rutas relacionadas con los canales
channel_bp.route('/<int:channel_id>', methods=['GET'])(ChannelController.get)
channel_bp.route('/create', methods=['POST'])(ChannelController.create)
channel_bp.route('/<int:channel_id>', methods=['DELETE'])(ChannelController.delete)

channel_bp.route('/server/<int:server_id>', methods=['GET'])(ChannelController.get_all)
