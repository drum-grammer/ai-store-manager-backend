from flask import jsonify
from http import HTTPStatus
from common.exception.custom_errors import CustomException


def handle_custom_error(error: CustomException):
    response = jsonify(
        {
            'code': error.error_code,
            'message': error.message
        }
    )
    response.status_code = error.status_code.value
    return response


def handle_unauthorized_error(error):
    response = jsonify(
        {
            'code': "GENERAL_" + HTTPStatus.UNAUTHORIZED.name,
            'message': error.message
        }
    )
    response.status_code = HTTPStatus.UNAUTHORIZED.value
    return response


def handle_forbidden_error(error):
    response = jsonify(
        {
            'code': "GENERAL_" + HTTPStatus.FORBIDDEN.name,
            'message': error.description,
        }
    )
    response.status_code = HTTPStatus.FORBIDDEN.value
    return response


def handle_not_found_error(error):
    response = jsonify(
        {
            'code': "GENERAL_" + HTTPStatus.NOT_FOUND.name,
            'message': error.description,
        }
    )
    response.status_code = HTTPStatus.NOT_FOUND.value
    return response


def handle_unexpected_error(error: Exception):
    response = jsonify(
        {
            'code': 'SYSTEM_ERROR',
            'message': f'예상치 못한 오류가 발생했습니다: {str(error)}'
        }
    )
    response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR.value
    return response
