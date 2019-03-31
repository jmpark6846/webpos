import secrets

import jwt
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from webpos_common.models import BaseModel
from webpos_common.utils import get_now


class Account(BaseModel, AbstractBaseUser):
    USERNAME_FIELD = "email"

    name = models.CharField('이름', max_length=40)
    email = models.CharField('이메일', max_length=128, unique=True)

    def __str__(self):
        return f"{self.name} <{self.email}>"


class AccessToken:
    EXPIRE_TIME = {'hours': 1}
    ALGORITHM = "HS256"

    def __init__(self, account:Account=None, value:str=None):
        if account:
            self.email = account.email

        if value:
            self.value = value

    def create_token(self):
        now = get_now()
        self.issued_at = now
        self.expire_at = now.add(**AccessToken.EXPIRE_TIME)

        payload = {
            'email': self.email,
            'iat': self.issued_at,
            'exp': self.expire_at
        }
        self.value = jwt.encode(payload=payload, key=settings.SECRET_KEY, algorithm=self.ALGORITHM)
        return self.value

    def decrypt_token(self):
        payload = jwt.decode(self.value, settings.SECRET_KEY, algorithms=[self.ALGORITHM,])
        self.email = payload['email']
        self.issued_at = payload['iat']
        self.expire_at = payload['exp']
        return payload


class RefreshToken(models.Model):
    EXPIRE_TIME = {'years': 1}
    value = models.CharField(max_length=43)
    issued_at = models.DateTimeField(auto_now_add=True)
    expire_at = models.DateTimeField(null=True)
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)

    def generate(self):
        self.value = self.generate_refresh_token()
        self.expire_at = get_now().add(**self.EXPIRE_TIME)
        self.save()

    def generate_refresh_token(self):
        return secrets.token_urlsafe(32)

    @property
    def is_expired(self):
        return self.expire_at > get_now()
