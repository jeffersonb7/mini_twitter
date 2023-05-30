from rest_framework import serializers
from .models import Account
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            'id', 
            'groups', 
            'user_permissions', 
            'is_staff',
            'is_active',
            'last_login',
            'is_superuser'
        )


class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Account
        fields = '__all__'

    def create(self, validated_data):
        username = validated_data['user']['username']
        password = validated_data['user']['password']
        email = validated_data['user']['email']

        account = None 

        try: 
            if User.objects.filter(username=username):
                raise serializers.ValidationError('The username or email is already exist')
            user_default = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )

            account = Account(
                birth_date=validated_data['birth_date'],
                user=user_default
            )
            account.save()
        except ValidationError as e:
            raise serializers.ValidationError('The username or email is already exist')
        
        return account
