from random import randint

from django.test import TestCase

from traders.models import Trader
from trading_accounts.models import TradingAccount


class TradingAccounts(TestCase):
    base_route = '/api/1.0/trading_accounts/'
    trader_username = 'trader'
    trader_password = 'trader_password'
    trading_accounts_count = randint(1, 10)

    def setUp(self):
        self.trader = Trader.objects.create_user(username=self.trader_username, password=self.trader_password)

    def test_trading_accounts_list_accounts_ok(self):
        self.client.login(username=self.trader_username, password=self.trader_password)
        self.create_trading_accounts()
        response = self.client.get(self.base_route)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), self.trading_accounts_count)

    def test_trading_accounts_list_accounts_is_empty_ok(self):
        self.client.login(username=self.trader_username, password=self.trader_password)
        response = self.client.get(self.base_route)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    def test_trading_accounts_list_accounts_not_logged_ko(self):
        response = self.client.get(self.base_route)
        self.assertEqual(response.status_code, 401)

    def create_trading_accounts(self):
        for i in range(self.trading_accounts_count):
            TradingAccount.objects.create(owner=self.trader)
