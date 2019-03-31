from webpos_account.models import Account, RefreshToken, AccessToken


def create_token(account: Account):
    access_token = AccessToken(account=account)
    access_token.create_token()
    refresh_token = RefreshToken.objects.create(account=account)
    refresh_token.generate()
    return access_token, refresh_token
