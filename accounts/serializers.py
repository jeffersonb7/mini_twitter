from rest_framework import serializers
from .models import Account
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         exclude = (
#             'id', 
#             'groups', 
#             'user_permissions', 
#             'is_staff',
#             'is_active',
#             'last_login',
#             'is_superuser'
#         )


class AccountCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    password = serializers.CharField(source='user.password')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.EmailField(source='user.email')

    class Meta:
        model = Account
        fields = (
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'about',
            'profile_picture',
            'birth_date',
        )

    def create(self, validated_data):
        username = validated_data['user']['username']
        password = validated_data['user']['password']
        first_name = validated_data['user']['first_name']
        last_name = validated_data['user']['last_name']
        email = validated_data['user']['email']

        account = None 

        try: 
            if User.objects.filter(username=username):
                raise serializers.ValidationError('The username or email is already exist')
            user_default = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name
            )

            account = Account(
                birth_date=validated_data['birth_date'],
                user=user_default,
            )
            if 'profile_picture' in validated_data:
                account.profile_picture =validated_data['profile_picture']
            account.save()
        except ValidationError as e:
            raise serializers.ValidationError('The username or email is already exist')
        
        return account
