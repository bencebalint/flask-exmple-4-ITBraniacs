from flask import Flask

from routes.add_route import AddPersonRoute
from routes.list_route import ListRoute
from routes.main_route import MainRoute
from routes.web_route import WebRoute


def main():
    app = Flask(__name__)

    routes = [
        MainRoute(),
        ListRoute(),
        AddPersonRoute(),
        WebRoute()
    ]

    for route in routes:
        app.add_url_rule(route.get_route(), view_func=route.as_view(route.get_route()))

    app.run()


if __name__ == '__main__':
    main()
