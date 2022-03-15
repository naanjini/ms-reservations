"""Entry point of our microservice. API endpoints (routes) are defined here.
 """

# pylint: disable=unused-import
import logging as log
import uuid
import json

from flask import Flask, request, jsonify, Response
from src import handlers, model

# pylint: disable=invalid-name
app = Flask(__name__)


@app.route('/hello/<name>', methods=['GET'])
def say_hello(name):
    """ Greeter Endpoint"""
    resp = handlers.greeter(name)
    return Response(resp, mimetype='plain/text')

# # For more sophisticated forms in Flask, see:
# # https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms
# @app.route('/users', defaults={'user_id': ""}, methods=['POST'])
# @app.route('/users/<user_id>', methods=['POST'])
# def update_user(user_id):
#     """Endpoint that creates or saves user in Redis database"""
#     # Note 'force=True' ignores mime-type=app/json requirement default in Flask
#     user = request.get_json(force=True)

#     resp = handlers.save_user(user, user_id)
#     return jsonify(resp)


@app.route('/reservations', methods=['PUT'])
def reserve():
    """Endpoint that reserves a seat for a customer"""
    json_body = request.get_json(force=True)
    resp = handlers.reserve(json_body)
    if (resp.get("status") == "success"):
        return jsonify(resp)
    else:
        return Response(
            json.dumps(resp),
            status=403,
            mimetype='application/json'
        )


@app.route('/reservations', methods=['GET'])
def reservations():
    """ Get Reservations Endpoint"""
    flight_id = request.args.get('flight_id')
    resp = handlers.get_reservations(flight_id)
    return jsonify(resp)


def init():
    """Init routine for the microservice"""
    uuid.uuid1()  # prime the uuid generator at startup


if __name__ == '__main__':
    init()

    app.run(debug=True, host='0.0.0.0')
