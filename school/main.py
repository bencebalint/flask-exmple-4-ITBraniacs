from flask import Flask

from routes.homepage_route import HomepageRoute
from routes.school_routes.add_route import AddPersonRoute
from routes.school_routes.list_route import ListRoute
from routes.main_route import MainRoute
from routes.web_route import WebRoute


app = Flask(__name__)
app.secret_key = 'secret'

routes = [
    MainRoute(),
    ListRoute(),
    AddPersonRoute(),
    WebRoute(),
    HomepageRoute()
]

for route in routes:
    app.add_url_rule(route.get_route(), view_func=route.as_view(route.get_route()))

app.run(host="0.0.0.0", port=8080, threaded=True, debug=True)
