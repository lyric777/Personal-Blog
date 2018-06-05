from flask import jsonify
from . import api
from app.exceptions import ValidationError

def bad_request(message):
    response = jsonify({'error': 'bad request', 'message': message})
    response.status_code = 400
    return response


def forbidden(message):
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_code = 403
    return response


def page_not_found(message):
    response = jsonify({'error': 'not_found', 'message': message})
    response.status_code = 404
    return response


def internal_server_error(message):
    response = jsonify({'error': 'internal_server_error', 'message': message})
    response.status_code = 500
    return response


@api.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])