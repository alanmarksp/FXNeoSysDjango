from django.db import models
from django.db.models import Max


class QuotesManager(models.Manager):

    def latest_quotes(self):
        quotes = self.model.objects.none()
        for symbol in self.model.SYMBOLS:
            q = self.model.objects.filter(symbol=symbol[0])
            latest_date = q.aggregate(datetime=Max('datetime'))
            quotes = quotes | q.filter(datetime=latest_date['datetime'])
        return quotes


class Quote(models.Model):
    EURUSD = 'EURUSD'
    GBPUSD = 'GBPUSD'
    USDJPY = 'USDJPY'
    USDCHF = 'USDCHF'
    SYMBOLS = (
        (EURUSD, 'Euro vs US Dollar'),
        (GBPUSD, 'Great Britain vs US Dollar'),
        (USDJPY, 'US Dollar vs Japanese Yen'),
        (USDCHF, 'US Dollar vs Swiss Franc')
    )
    symbol = models.CharField(
        max_length=6,
        choices=SYMBOLS
    )
    bid_price = models.DecimalField(max_digits=10, decimal_places=4)
    ask_price = models.DecimalField(max_digits=10, decimal_places=4)
    datetime = models.DateTimeField(auto_now_add=True)
    objects = QuotesManager()
