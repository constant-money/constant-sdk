from rest_framework import status
from rest_framework.exceptions import APIException


class UnexpectedException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Unexpected error'
    default_code = 'unexpected_error'


class InvalidDataException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Invalid data'
    default_code = 'invalid_data'


class InvalidInputDataException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Invalid input data'
    default_code = 'invalid_input_data'


class InvalidAddressException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Invalid address'
    default_code = 'invalid_address'


class InvalidTransactionException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Invalid transaction'
    default_code = 'invalid_transaction'


class TxHashNotFoundException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Transaction has not found'
    default_code = 'tx_hash_not_found'
