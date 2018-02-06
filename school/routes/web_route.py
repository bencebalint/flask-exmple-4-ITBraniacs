from flask import Response, send_file

from routes.main_route import MainRoute


class WebRoute(MainRoute):

    def __init__(self):
        super().__init__()

    @classmethod
    def _generate_response(cls, input_data=None) -> Response:
        return super()._generate_response(input_data)

    def get(self, element: str) -> Response:
        location = ""
        if element.__contains__("js"):
            location = "templates/script/"
        elif element.__contains__("css"):
            location = "templates/css/"

        return send_file(location + element)

    def post(self) -> Response:
        return super().post()

    def delete(self) -> Response:
        return super().delete()

    def put(self) -> Response:
        return super().put()

    def get_route(self) -> str:
        return "/<string:element>"
