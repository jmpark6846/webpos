from django.urls import reverse
from rest_framework.test import APITestCase

from webpos_account.models import Account


class AccountTestCase(APITestCase):
    def setUp(self):
        self.account_data = {
            'email': 'test@test.co.kr',
            'name': 'test',
            'password': 'password',
        }

    def test_login(self):
        res = self.client.post(reverse('webpos_account:account-create'), data=self.account_data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(Account.objects.filter(email=self.account_data['email']).exists())

        res = self.client.post(reverse('webpos_account:token'), data=self.account_data)
        self.assertEqual(res.status_code, 200)
        self.assertIsNotNone(res.data['body']['token'])
