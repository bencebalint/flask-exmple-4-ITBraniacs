from flask import request, Response

from element.person import Person
from routes.main_route import MainRoute


class AddPersonRoute(MainRoute):

    def __init__(self):
        super().__init__()

    @classmethod
    def _generate_response(cls, input_data=None) -> Response:
        return super()._generate_response(input_data=input_data)

    def get(self) -> Response:
        return super().get()

    def post(self) -> Response:
        name = request.form["name"]
        address = request.form["address"]
        person: Person = Person(name=name, address=address)

        status = super()._school.get_list().add(person)
        return self._generate_response(input_data="add_status: " + str(status))

    def delete(self) -> Response:
        return super().delete()

    def put(self) -> Response:
        return super().put()

    def get_route(self) -> str:
        return "/add/person"
