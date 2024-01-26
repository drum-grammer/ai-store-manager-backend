from flask_jwt_extended import create_access_token

from common.enum.user_type import UserType
from config import JWTConfig


def generate_token(
    user_id: str,
    scope: str = UserType.TEAM_MEMBER.name,
) -> str:
    user_data = {
        'user_id': user_id,
        'scope': scope,
    }

    access_token = create_access_token(
        identity=user_id,
        additional_claims=user_data,
        expires_delta=JWTConfig.instance().ACCESS_TOKEN_EXPIRES_IN
    )
    return access_token
