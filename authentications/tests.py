import random
import string

from django.test import TestCase

from traders.models import Trader


class Authentication(TestCase):
    base_route = '/api/1.0/authenticate/'

    @staticmethod
    def getLongString(length):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    def setUp(self):
        self.trader_username = 'trader'
        self.trader_password = 'trader_password'
        self.new_trader_username = 'new_trader'
        self.new_trader_password = 'new_trader_password'
        self.long_username = self.getLongString(256)
        self.long_password = self.getLongString(256)
        self.invalid_characters_username = "$trader$"

        self.trader = Trader.objects.create_user(username=self.trader_username, password=self.trader_password)

    def test_login_ok(self):
        response = self.client.post('{}login/'.format(self.base_route), data={'username': self.trader_username,
                                                                              'password': self.trader_password})
        self.assertEqual(response.status_code, 200)

    def test_login_invalid_username_ko(self):
        response = self.client.post('{}login/'.format(self.base_route), data={'username': 'invalid_username',
                                                                              'password': self.trader_password})
        self.assertEqual(response.status_code, 400)

    def test_login_invalid_password_ko(self):
        response = self.client.post('{}login/'.format(self.base_route), data={'username': self.trader_username,
                                                                              'password': 'invalid_passwrod'})
        self.assertEqual(response.status_code, 400)

    def test_login_invalid_username_and_password_ko(self):
        response = self.client.post('{}login/'.format(self.base_route), data={'username': 'invalid_username',
                                                                              'password': 'invalid_passwrod'})
        self.assertEqual(response.status_code, 400)

    def test_register_ok(self):
        response = self.client.post('{}register/'.format(self.base_route), data={'username': self.new_trader_username,
                                                                                 'password': self.new_trader_password})
        self.assertEqual(response.status_code, 200)

    def test_register_username_already_in_use_ko(self):
        response = self.client.post('{}register/'.format(self.base_route), data={'username': self.new_trader_username,
                                                                                 'password': self.new_trader_password})
        self.assertEqual(response.status_code, 200)

    def test_register_long_username_ko(self):
        response = self.client.post('{}register/'.format(self.base_route), data={'username': self.long_username,
                                                                                 'password': self.new_trader_password})
        self.assertEqual(response.status_code, 400)

    def test_register_long_password_ko(self):
        response = self.client.post('{}register/'.format(self.base_route), data={'username': self.new_trader_username,
                                                                                 'password': self.long_password})
        self.assertEqual(response.status_code, 400)

    def test_register_long_username_and_long_password_ko(self):
        response = self.client.post('{}register/'.format(self.base_route), data={'username': self.long_username,
                                                                                 'password': self.long_password})
        self.assertEqual(response.status_code, 400)

    def test_register_username_with_invalid_characters_ko(self):
        response = self.client.post('{}register/'.format(self.base_route),
                                    data={'username': self.invalid_characters_username,
                                          'password': self.new_trader_password})
        self.assertEqual(response.status_code, 400)
