from unittest.mock import MagicMock

from rest_framework.test import APIClient

from integration_3rdparty.const import ConstantManagement


class AuthenticationUtils(object):
    def __init__(self, client: APIClient, username: str = 'test_username@email.com'):
        self.client = client
        self.username = username

    def user_login(self, username: str = None):
        username = username if username else self.username
        ConstantManagement.get_profile = MagicMock(return_value={
            'Result': {
                'ID': 1,
                'UserName': username,
                'FullName': username,
                'Email': username,
                'RoleID': 0,
                'ConstantBalance': 0,
                'ConstantBalanceHolding': 0,
                'VerifiedLevel': 0,
                'DOB': '',
                'AddressCountry': 'US',
            }
        })
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + username)

    def admin_login(self, username: str = None):
        username = username if username else self.username
        ConstantManagement.get_profile = MagicMock(return_value={
            'Result': {
                'ID': 1,
                'UserName': username,
                'FullName': username,
                'Email': username,
                'RoleID': 1,
                'ConstantBalance': 0,
                'ConstantBalanceHolding': 0,
                'VerifiedLevel': 0,
                'DOB': '',
                'AddressCountry': 'US',
            }
        })
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + username)

    def agent_login(self, username: str = None):
        username = username if username else self.username
        ConstantManagement.get_profile = MagicMock(return_value={
            'Result': {
                'ID': 1,
                'UserName': username,
                'FullName': username,
                'Email': username,
                'RoleID': 1,
                'ConstantBalance': 0,
                'ConstantBalanceHolding': 0,
                'VerifiedLevel': 0,
                'DOB': '',
                'AgentUser': True,
                'AddressCountry': 'US',
            }
        })
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + username)
