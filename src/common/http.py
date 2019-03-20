from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import exception_handler


class StandardPagination(PageNumberPagination):
    page_size = 100
    max_page_size = 1000
    page_size_query_param = 'page_size'


class SuccessResponse(Response):
    def __init__(self, data=None, code=None, message=None, default_status=None,
                 template_name=None, headers=None,
                 exception=False, content_type=None):
        selected_status = default_status if default_status else status.HTTP_200_OK
        wrapped_data = {
            'code': code if code else 1,
            'message': message if message else "OK",
            'status': selected_status,
            "data": data,
        }
        super(SuccessResponse, self).__init__(wrapped_data, selected_status, template_name, headers, exception,
                                              content_type)


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None and response.status_code == 400:
        if not type(response.data) is list:
            response.data['status'] = response.status_code
            if 'detail' in response.data:
                response.data['message'] = response.data['detail']
                response.data['code'] = exc.get_codes()
                del response.data['detail']
            else:
                response.data['message'] = 'Validation error'
                response.data['code'] = 'validation_error'
        else:
            response.data = {
                'message': 'Validation error',
                'code': 'validation_error',
                'details': response.data,
            }

    return response
