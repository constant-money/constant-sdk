from django.contrib.auth.models import User
from django.db import models


class ConstUser(User):
    class Meta:
        managed = False

    user_id = models.IntegerField()
    user_name = models.CharField(max_length=255)
    api_token = models.CharField(max_length=255)
