from flask import Flask
from flask_cors import CORS
from config import Config

from .routes.user_bp import user_bp
from .routes.server_bp import server_bp
from .routes.error_handlers import errors
from .routes.channel_bp import channel_bp
from .routes.message_bp import message_bp
from .routes.category_bp import category_bp
from .routes.role_permission_bp import role_permission_bp
from .routes.member_bp import member_bp

from .database import DatabaseConnection


def init_api():
    """Crea y configura la aplicación Flask"""

    api = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)

    CORS(api, supports_credentials=True)

    api.config.from_object(
        Config
    )

    DatabaseConnection.set_config(api.config)

    api.register_blueprint(user_bp, url_prefix='/user')
    api.register_blueprint(server_bp, url_prefix='/server')
    api.register_blueprint(errors, url_prefix='/errors')
    api.register_blueprint(channel_bp, url_prefix='/channel')
    api.register_blueprint(message_bp, url_prefix='/message')
    api.register_blueprint(category_bp, url_prefix='/category')
    api.register_blueprint(role_permission_bp, url_prefix='/role_permission')
    api.register_blueprint(member_bp, url_prefix='/member')

    return api
