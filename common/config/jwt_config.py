from flask_jwt_extended import JWTManager


def init_jwt(base_app):
    jwt = JWTManager()
    jwt.init_app(base_app)

