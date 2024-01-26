import datetime
from functools import wraps

from flask_jwt_extended import get_jwt, create_access_token, verify_jwt_in_request

from common.enum.user_type import UserType
from common.exception.custom_errors import CustomError
from common.util.logger import logger


def admin_scope_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        scope = get_jwt().get('scope')
        if scope != UserType.ADMIN_USER.name:
            raise CustomError.ADMIN_AUTHORITY_REQUIRED.value
        else:
            return func(*args, **kwargs)

    return wrapper


def team_leader_scope_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        scope = get_jwt().get('scope')
        if scope != UserType.TEAM_LEADER.name:
            raise CustomError.TEAM_LEADER_AUTHORITY_REQUIRED.value
        else:
            return func(*args, **kwargs)

    return wrapper


def team_leader_or_admin_scope_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        scope = get_jwt().get('scope')
        if scope not in [UserType.TEAM_LEADER.name, UserType.ADMIN_USER.name]:
            raise CustomError.TEAM_LEADER_AUTHORITY_REQUIRED.value
        else:
            return func(*args, **kwargs)

    return wrapper


def team_member_scope_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        scope = get_jwt().get('scope')
        if scope != UserType.TEAM_MEMBER.name:
            raise CustomError.TEAM_MEMBER_AUTHORITY_REQUIRED.value
        else:
            return func(*args, **kwargs)

    return wrapper


def user_scope_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        scope = get_jwt().get('scope')
        if scope not in UserType.name_list():
            raise CustomError.INVALID_TOKEN.value
        else:
            return func(*args, **kwargs)

    return wrapper


def jwt_optional(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if verify_jwt_in_request(optional=True):
            scope = get_jwt().get('scope')
            logger.debug(f'jwt is exist. scope : {scope}')
        else:
            logger.debug('jwt is not exist')
        return func(*args, **kwargs)

    return wrapper
