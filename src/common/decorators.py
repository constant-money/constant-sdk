import functools
import logging

from rest_framework.exceptions import APIException


def raise_api_exception(exception: APIException):
    def handle_exception(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logging.exception(e)
                raise exception

        return wrapper

    return handle_exception
