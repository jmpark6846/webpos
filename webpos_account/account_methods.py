import secrets

import jwt
from django.conf import settings

from webpos_account.models import Account
from webpos_common.utils import get_now


def create_jwt(account:Account):
    now = get_now()
    payload={
        'email':account.email,
        'iat': now,
        'exp': now.add(**RefreshToken.EXPIRE_TIME)
    }
    access_token = jwt.encode(payload=payload, key=settings.SECRET_KEY, algorithm='HS256')
    refresh_token = RefreshToken(token=generate_refresh_token())

    return access_token, refresh_token


def decrypt_token(token: str):
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    return payload


def generate_refresh_token():
    return secrets.token_urlsafe(32)

