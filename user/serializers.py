from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Account
from rest_framework.authtoken.views import Token

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'email', 'password']

        extra_kwargs = {'password':{
            'write_only': True,
            'required':True
        }}

    '''
    def create(self, validated_data):
        user = Account.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
    '''
    
