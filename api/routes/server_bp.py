from flask import Blueprint
from ..controllers.server_controller import ServerController


server_bp = Blueprint('server_bp', __name__)

server_bp.route('/<int:server_id>', methods=['GET'])(ServerController.get)
server_bp.route('/', methods=['GET'])(ServerController.get_all)
server_bp.route('/createserver', methods=['POST'])(ServerController.create)

server_bp.route('/list_user/<int:user_id>', methods=['GET'])(ServerController.get_all_server)