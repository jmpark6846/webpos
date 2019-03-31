from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from webpos_account.models import Account


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
