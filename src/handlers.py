""" Endpoint Callback Handlers """

import logging as log
import uuid
import json

from . import model


def greeter(name):
    """Greeter route callback"""
    return f"Hello {name}!"

# def save_user(user, user_id=""):
#     """Save User route callback"""
#     if user_id == "":
#         user_id = str(uuid.uuid4())
#     log.info("Saving USER_ID: %s", user_id)

#     user = json.dumps(user)

#     return model.save_user(user, user_id)


def reserve(json_body):
    """Save reservation callback"""
    return model.save_reservation(json_body)


def get_reservations(flight_id):
    """Get reservations callback"""
    return model.get_reservations(flight_id)
