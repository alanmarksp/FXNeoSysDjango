from django.db import models

from traders.models import Trader


class TradingAccount(models.Model):
    funds = models.DecimalField(name='funds', max_digits=12, decimal_places=2, default=10000.00)
    realized_profit = models.DecimalField(name='realized profit', max_digits=10, decimal_places=2, default=0)
    owner = models.ForeignKey(Trader, name='owner', related_name='trading_accounts')
