from rest_framework import authentication
from rest_framework.authentication import get_authorization_header

from constant_core.business import ConstantCoreBusiness
from sdk.models import ConstUser


class SdkAuthentication(authentication.BaseAuthentication):
    keyword = ''

    def authenticate(self, request):
        auth = get_authorization_header(request)
        token = auth.decode()

        const_user = ConstantCoreBusiness.get_user_by_api_token(token)
        user = ConstUser(
            user_id=const_user.id,
            user_name=const_user.user_name,
            api_token=const_user.api_token,
        )

        return user, None
