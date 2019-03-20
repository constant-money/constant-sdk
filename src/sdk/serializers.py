from decimal import Decimal

from rest_framework import serializers


class TransferSerializer(serializers.Serializer):
    class Meta:
        fields = ('user_id', 'to_email', 'amount', 'api_token')

    user_id = serializers.IntegerField()
    to_email = serializers.EmailField()
    amount = serializers.DecimalField(max_digits=18, decimal_places=2)
    api_token = serializers.CharField()

    def validate_amount(self, value):
        if Decimal(value) < Decimal(0.01):
            raise serializers.ValidationError('Must be greater than 0')

        return value
