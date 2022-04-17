from flask import render_template
from flask_restplus import Resource
from src.server.instance import server
from src.server.instance import application


@application.route("/health")
def index():
  return render_template('anya_is_alive.html')