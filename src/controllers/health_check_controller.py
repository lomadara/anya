from flask import render_template
from flask_restplus import Resource
from src.server.instance import server


health_check = server.health_check


@health_check.route('/', methods=['GET'])
class HealthCheckController(Resource):
    def get(self):
        return render_template("anya_is_alive.html")