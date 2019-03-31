from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from webpos_common.models import BaseModel


class Account(BaseModel, AbstractBaseUser):
    USERNAME_FIELD = "email"

    name = models.CharField('이름', max_length=40)
    email = models.CharField('이메일', max_length=128, unique=True)

    def __str__(self):
        return f"{self.name} <{self.email}>"


class TokenManager(models.Manager):
    def create(self):


class RefreshToken(models.Model):
    objects = TokenManager()
    EXPIRE_TIME = {'hours': 1}
    token = models.CharField('Refresh 토큰', max_length=32)
