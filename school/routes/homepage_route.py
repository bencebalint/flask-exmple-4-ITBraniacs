from flask import Response, render_template

from routes.main_route import MainRoute


class HomepageRoute(MainRoute):

    def __init__(self):
        super().__init__()

    @classmethod
    def _generate_response(cls, input_data=None) -> Response:
        return super()._generate_response(input_data)

    def get(self) -> Response:
        return render_template("index.html")

    def post(self) -> Response:
        return super().post()

    def delete(self) -> Response:
        return super().delete()

    def put(self) -> Response:
        return super().put()

    def get_route(self) -> str:
        return "/homepage"
