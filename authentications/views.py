from django.contrib.auth import authenticate, login as django_login
from rest_framework.authtoken.models import Token
from rest_framework.decorators import list_route
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from authentications.serializers import AuthenticationSerializer
from traders.models import Trader
from traders.serializers import TraderSerializer


class AuthenticationView(GenericViewSet):
    serializer_class = AuthenticationSerializer

    @list_route(methods=['POST'])
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        trader = authenticate(**serializer.validated_data)

        if trader:
            if not trader.is_active:
                msg = 'User account is disabled.'
                raise ValidationError(msg, code='authorization')
        else:
            msg = 'Unable to log in with provided credentials.'
            raise ValidationError(msg, code='authorization')
        token = self.perform_login(request, trader)
        return Response({'token': token.key})

    @list_route(methods=['POST'])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        trader_serializer = TraderSerializer(data=serializer.validated_data)
        trader_serializer.is_valid(raise_exception=True)
        trader = Trader.objects.create_user(**trader_serializer.validated_data)
        token = self.perform_login(request, trader)
        return Response({'token': token.key})

    @staticmethod
    def perform_login(request, trader):
        token, created = Token.objects.get_or_create(user=trader)
        django_login(request, trader)
        return token
