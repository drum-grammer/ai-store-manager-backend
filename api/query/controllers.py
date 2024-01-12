from flask_restx import Namespace, fields, Resource

from api.query.service import query_to_llm

query_api = Namespace('llm', description='메시지 API')

query_message_request = query_api.model('query_message_request', {
    'message': fields.String(required=True, title='질문'),
})

query_message_response = query_api.model('query_message_response', {
    'result': fields.String(required=True, title='답변'),
})


@query_api.route("/query")
class QueryCls(Resource):
    @query_api.expect(query_message_request)
    @query_api.marshal_with(query_message_response, envelope='data')
    def post(self):
        return {'result': query_to_llm(query_api.payload['message'])}