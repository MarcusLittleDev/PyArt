from rest_framework import serializers
from . import models
from django.contrib.auth import authenticate

class CreateUserProfileSerializer(serializers.ModelSerializer):
    """A serializer for user profile objects"""
    confirm_password = serializers.CharField(allow_blank=False, write_only=True)

    class Meta: 
        model = models.UserProfile
        fields = ('id', 'username', 'email', 'password', 'confirm_password')
        extra_kwargs = {'password':{'write_only':True}}

    def validate(self, data):
        """Checks to to see if password and confirm_password are the same"""
        if data['password'] != data.pop('confirm_password'):
            raise serializers.ValidationError('Passwords do not match!')
        return data

    def create(self, validated_data):
        """Create and return a new user"""

        user = models.UserProfile(
            username=validated_data['username'],
            email = validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class UserSerializer(serializers.ModelSerializer):
    """used to return the output after user has succesfully registered."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'username')

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")