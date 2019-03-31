from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed

from webpos_account.account_methods import decrypt_token
from webpos_account.models import Account



class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        access_token = request.META.get('HTTP_X_AUTHORIZATION', None)

        if not access_token:
            return None

        payload = decrypt_token(access_token)
        account = Account.objects.filter(email=payload['email'], deleted_at=None)

        if not account.exists():
            raise AuthenticationFailed

        account = account.last()
        return account, access_token

