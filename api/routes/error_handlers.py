from flask import Blueprint
from ..models.exceptions import InvalidDataError

errors = Blueprint("errors",__name__)

@errors.app_errorhandler(InvalidDataError)
def handle_user_bad(error):
    return error.get_response(), error.status_code