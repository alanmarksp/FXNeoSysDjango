from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from traders.models import Trader
from traders.serializers import TraderSerializer


class TraderView(GenericViewSet):
    queryset = Trader.objects.all()
    serializer_class = TraderSerializer

    @list_route(methods=['GET', 'PUT', 'PATCH'])
    def profile(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        if request.method == 'GET':
            return Response(serializer.data)
        else:
            self.kwargs['pk'] = request.user.id
            if request.method == 'PUT':
                return self.update(request, *args, **kwargs)
            else:
                return self.partial_update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

