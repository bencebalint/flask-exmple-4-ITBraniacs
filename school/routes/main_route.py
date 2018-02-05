from flask import Response, json, redirect, url_for
from flask.views import MethodView

from elements.school_list import SchoolList


class MainRoute(MethodView):

    _school = SchoolList()

    def __init__(self):
        pass

    @classmethod
    def _generate_response(cls, input_data=None) -> Response:
        if input_data is None:
            resp = dict(status=1, content="Method Not Implemented!")
        else:
            resp = dict(status=0, content=input_data)
        return Response(json.dumps(resp))

    def get(self) -> Response:
        return redirect(url_for('/homepage'))

    def post(self) -> Response:
        return self._generate_response()

    def delete(self) -> Response:
        return self._generate_response()

    def put(self) -> Response:
        return self._generate_response()

    def get_route(self) -> str:
        return "/"
