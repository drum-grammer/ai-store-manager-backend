from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restx import Api

authorizations = {
    'user_token': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': 'JWT for User'
    },
}


def create_app():
    flask_app = Flask(__name__)
    api = Api(
        flask_app,
        authorizations=authorizations,
        security='user_token',
        doc='/swagger',
        title='AI STORE MANAGER API',
        version='1.0',
        description='AI Store Manager API'
    )
    flask_app.config["PROPAGATE_EXCEPTIONS"] = True
    flask_app.config["JWT_SECRET_KEY"] = 'this is key.'  # 시크릿은 비밀로 해야합니다.
    jwt = JWTManager()
    jwt.init_app(flask_app)

    from api.llm.controllers import llm_api

    api.add_namespace(llm_api)

    CORS(flask_app)

    return flask_app


app = create_app()


@app.errorhandler(Exception)
def handle_root_exception(error):
    import traceback
    traceback.print_exc()
    try:
        message = error.message
    except AttributeError:
        message = str(error)
    print(f"ErrorHandler {error}")
    return {'message': message, 'error': error.__class__.__name__}, 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
