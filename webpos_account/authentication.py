from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed

from webpos_account.models import Account, AccessToken


class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        _access_token = request.META.get('HTTP_X_AUTHORIZATION', None)

        if not _access_token:
            return None

        access_token = AccessToken(value=_access_token)
        access_token.decrypt_token()

        account = Account.objects.filter(email=access_token.email, deleted_at=None)

        if not account.exists():
            raise AuthenticationFailed

        account = account.last()
        return account, access_token.value

