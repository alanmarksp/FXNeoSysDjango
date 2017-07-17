from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from quotes.models import Quote
from quotes.serializers import QuoteSerializer


class QuoteView(GenericViewSet, ListModelMixin):
    queryset = Quote.objects.latest_quotes()
    serializer_class = QuoteSerializer
