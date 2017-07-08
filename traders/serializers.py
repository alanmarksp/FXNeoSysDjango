from rest_framework import serializers

from traders.models import Trader


class TraderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trader
        fields = ('username', 'email', 'first_name', 'last_name')
