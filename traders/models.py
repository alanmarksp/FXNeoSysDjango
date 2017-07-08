from django.contrib.auth.models import AbstractUser
from django.db import models


class Trader(AbstractUser):
    selected_trading_account = models.ForeignKey(
        'trading_accounts.TradingAccount',
        name='selected_trading_account',
        null=True,
        blank=True
    )
