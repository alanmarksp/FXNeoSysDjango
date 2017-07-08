from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from traders.models import Trader
from traders.serializers import TraderSerializer


class TraderView(GenericViewSet):
    queryset = Trader.objects.all()
    serializer_class = TraderSerializer

    @list_route(methods=['GET'])
    def profile(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


