from http import HTTPStatus

from flask_restx import Namespace, fields, Resource

from api.llm.service import query_to_llm, get_query_result

llm_api = Namespace('llm', description='메시지 API')

query_message_request = llm_api.model('query_message_request', {
    'query_id': fields.String(required=True, title='질문 ID'),
    'message': fields.String(required=True, title='질문'),
})

query_message_response = llm_api.model('query_message_response', {
    'result': fields.String(required=True, title='답변'),
})


@llm_api.route("/query")
class LLMQuery(Resource):
    @llm_api.expect(query_message_request)
    @llm_api.marshal_with(query_message_response)
    def post(self):
        return {
            'result': query_to_llm(
                llm_api.payload['query_id'],
                llm_api.payload['message']
            )
        }


query_result_request = llm_api.model('query_result_request', {
    'query_id': fields.String(required=True, title='질문 ID'),
})


@llm_api.route("/query-result/<string:query_id>")
class QueryResult(Resource):
    @llm_api.expect(query_result_request)
    @llm_api.marshal_with(query_message_response)
    def get(self, query_id):
        return {'result': get_query_result(query_id)}


@llm_api.route('/health-check', strict_slashes=False)
class HealthCheck(Resource):
    @llm_api.doc(security=None, description='헬스 체크 API')
    @llm_api.response(code=HTTPStatus.OK.value, description='서버가 정상적으로 구동 되고 있음')
    def get(self) -> HTTPStatus:
        return HTTPStatus.OK
