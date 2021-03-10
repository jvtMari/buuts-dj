from rest_framework import serializers, pagination
#
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
#
from .models import User


class GetUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'name',
            'surnames',
            'gender',
            'date_birth',
            'phone',
            'adress',
            'cp',
            'city',
            'country'
        )


class PostUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'name',
            'surnames',
            'gender',
            'date_birth',
            'phone',
            'adress',
            'cp',
            'city',
            'country'
        )

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data.get('email'),
            validated_data.get('name'),
            validated_data.get('surnames'),
            validated_data.get('password'),
            gender = validated_data.get('gender'),
            date_birth = validated_data.get('date_birth'),
            phone = validated_data.get('phone'),
            adress = validated_data.get('adress'),
            cp = validated_data.get('cp'),
            city = validated_data.get('city'), 
            country = validated_data.get('country') 
        )
        Group.objects.get(name='clients').user_set.add(user)
        return user


class PatchUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'email',
            'name',
            'surnames',
            'gender',
            'date_birth',
            'phone',
            'adress',
            'cp',
            'city',
            'country',
        )
    
    def validate(self, data):
        user_token = self.context.get('request', None).user

        if user_token != self.instance:
            raise serializers.ValidationError(
                "Not Authorized. The user id is not applicable to user token. ")

        return super().validate(data)


class ChangePassUserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate(self, data):
        user_token = self.context.get('request', None).user
        
        if (user_token != self.instance):
            raise serializers.ValidationError(
                "Not Authorized. The user id is not applicable to user token. ")

        auth_user = authenticate(
            email = data.get('email'),
            password = data.get('password')
        )
        if auth_user is None:    
            raise serializers.ValidationError(
                "The current password is not correct.")

        return super().validate(data)

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('new_password'))
        instance.save()

        return instance

    def to_representation(self, instance):
        return {
            'email' : instance.email,
            'msg' : 'Password changed successfully'
        }


class UserPagination(pagination.PageNumberPagination):
    page_size = 10
    max_page_size = 100
