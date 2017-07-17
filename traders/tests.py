from django.test import TestCase

from traders.models import Trader


class Traders(TestCase):
    base_route = '/api/1.0/traders/'
    trader_username = 'trader'
    trader_password = 'trader_password'

    def setUp(self):
        self.trader = Trader.objects.create_user(username=self.trader_username, password=self.trader_password)

    def test_traders_profile_ok(self):
        self.client.login(username=self.trader_username, password=self.trader_password)
        response = self.client.get('{}profile/'.format(self.base_route))
        self.assertEqual(response.status_code, 200)

    def test_traders_profile_not_logged_ko(self):
        response = self.client.get('{}profile/'.format(self.base_route))
        self.assertEqual(response.status_code, 401)
