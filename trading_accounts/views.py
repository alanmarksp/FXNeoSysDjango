from django.http import Http404
from rest_framework.decorators import list_route
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from trading_accounts.models import TradingAccount
from trading_accounts.serializers import TradingAccountSerializer


class TradingAccountView(GenericViewSet, ListModelMixin):
    serializer_class = TradingAccountSerializer

    def get_queryset(self):
        return TradingAccount.objects.filter(owner=self.request.user)

    @list_route(methods=['GET'])
    def selected(self, request):
        selected_trading_account = request.user.selected_trading_account
        if not selected_trading_account:
            raise Http404

        serializer = self.get_serializer(selected_trading_account)
        return Response(serializer.data)
