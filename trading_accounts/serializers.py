from rest_framework import serializers

from trading_accounts.models import TradingAccount


class TradingAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradingAccount
        fields = '__all__'
