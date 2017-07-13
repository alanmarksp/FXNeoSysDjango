from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from traders.models import Trader


class TradingAccount(models.Model):
    funds = models.DecimalField(name='funds', max_digits=12, decimal_places=2, default=10000.00)
    realized_profit = models.DecimalField(name='realized_profit', max_digits=10, decimal_places=2, default=0)
    owner = models.ForeignKey(Trader, name='owner', related_name='trading_accounts')


@receiver(post_save, sender=TradingAccount)
def save_trading_account(sender, instance, **kwargs):
    trader = instance.owner
    if not trader.selected_trading_account:
        trader.selected_trading_account = instance
        trader.save()
