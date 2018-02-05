from flask import Response

from routes.main_route import MainRoute


class ListRoute(MainRoute):

    def __init__(self):
        super().__init__()

    @classmethod
    def _generate_response(cls, input_data=None) -> Response:
        return super()._generate_response(input_data=input_data)

    def get(self) -> Response:
        ret_list = []
        m_list = super()._school.get_list().get_iterator()
        while m_list.has_next():
            ret_list.append(str(m_list.next()))
        return self._generate_response(input_data=ret_list)

    def post(self) -> Response:
        return super().post()

    def delete(self) -> Response:
        return super().delete()

    def put(self) -> Response:
        return super().put()

    def get_route(self) -> str:
        return "/list"

