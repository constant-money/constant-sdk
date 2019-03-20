from decimal import Decimal

from django.conf import settings
from django.db import models
from django.utils import timezone


class ConstantManager(models.Manager):
    def get_queryset(self):
        return models.QuerySet(self.model, using='constant')


class User(models.Model):
    class Meta:
        db_table = 'users'
        managed = False

    id = models.PositiveIntegerField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    user_name = models.CharField(max_length=255, blank=True)
    full_name = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255)
    constant_balance = models.BigIntegerField(default=0)
    constant_balance_holding = models.BigIntegerField(default=0)
    pro_saving_user = models.BooleanField(default=False)
    agent_user = models.BooleanField(default=False)
    address_country = models.CharField(max_length=255, blank=True)

    status = models.IntegerField(default=1)
    user_role_id = models.IntegerField(default=0)
    type = models.IntegerField(default=0)
    verified_level = models.IntegerField(default=0)
    account_type = models.IntegerField(default=0)
    gender = models.IntegerField(default=1)
    primetrust_contact_status = models.IntegerField(default=-1)
    referral_code = models.CharField(max_length=255, blank=True)
    social_type = models.IntegerField(default=0)
    is_reset_password = models.IntegerField(default=0)
    reset_password_token = models.CharField(max_length=255)
    api_token = models.CharField(max_length=255)

    objects = ConstantManager()

    @property
    def constant_balance_friendly(self):
        return self.constant_balance / Decimal(100)

    @property
    def constant_balance_holding_friendly(self):
        return self.constant_balance_holding / Decimal(100)

    @property
    def language(self):
        return settings.COUNTRY_LANGUAGE_CODE.get(self.address_country, 'en')
