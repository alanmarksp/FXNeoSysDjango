import random
import string

from django.test import TestCase

from traders.models import Trader


class Authentications(TestCase):
    base_route = '/api/1.0/authentications/'
    trader_username = 'trader'
    trader_password = 'trader_password'
    new_trader_username = 'new_trader'
    new_trader_password = 'new_trader_password'
    invalid_characters_username = "$trader$"

    def setUp(self):
        self.trader = Trader.objects.create_user(username=self.trader_username, password=self.trader_password)

    def test_authentications_login_ok(self):
        response = self.client.post('{}login/'.format(self.base_route), data={'username': self.trader_username,
                                                                              'password': self.trader_password})
        self.assertEqual(response.status_code, 200)

    def test_authentications_login_invalid_username_ko(self):
        response = self.client.post('{}login/'.format(self.base_route), data={'username': 'invalid_username',
                                                                              'password': self.trader_password})
        self.assertEqual(response.status_code, 400)

    def test_authentications_login_invalid_password_ko(self):
        response = self.client.post('{}login/'.format(self.base_route), data={'username': self.trader_username,
                                                                              'password': 'invalid_passwrod'})
        self.assertEqual(response.status_code, 400)

    def test_authentications_login_invalid_username_and_password_ko(self):
        response = self.client.post('{}login/'.format(self.base_route), data={'username': 'invalid_username',
                                                                              'password': 'invalid_passwrod'})
        self.assertEqual(response.status_code, 400)

    def test_authentications_register_ok(self):
        response = self.client.post('{}register/'.format(self.base_route), data={'username': self.new_trader_username,
                                                                                 'password': self.new_trader_password})
        self.assertEqual(response.status_code, 200)

    def test_authentications_register_username_already_in_use_ko(self):
        response = self.client.post('{}register/'.format(self.base_route), data={'username': self.new_trader_username,
                                                                                 'password': self.new_trader_password})
        self.assertEqual(response.status_code, 200)

    def test_authentications_register_long_username_ko(self):
        response = self.client.post('{}register/'.format(self.base_route), data={'username': self.getLongString(256),
                                                                                 'password': self.new_trader_password})
        self.assertEqual(response.status_code, 400)

    def test_authentications_register_long_password_ko(self):
        response = self.client.post('{}register/'.format(self.base_route), data={'username': self.new_trader_username,
                                                                                 'password': self.getLongString(256)})
        self.assertEqual(response.status_code, 400)

    def test_authentications_register_long_username_and_long_password_ko(self):
        response = self.client.post('{}register/'.format(self.base_route), data={'username': self.getLongString(256),
                                                                                 'password': self.getLongString(256)})
        self.assertEqual(response.status_code, 400)

    def test_authentications_register_username_with_invalid_characters_ko(self):
        response = self.client.post('{}register/'.format(self.base_route),
                                    data={'username': self.invalid_characters_username,
                                          'password': self.new_trader_password})
        self.assertEqual(response.status_code, 400)

    @staticmethod
    def getLongString(length):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
