from constant_core.models import User


class ConstantCoreBusiness(object):
    @staticmethod
    def get_user(user_id: int):
        return User.objects.get(id=user_id)

    @staticmethod
    def get_user_by_email(email: str):
        return User.objects.filter(email=email).first()

    @staticmethod
    def get_user_by_api_token(api_token: str):
        return User.objects.filter(api_token=api_token).first()
