"""Movie Serializers"""
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Movie


class RegisterSerializer(serializers.ModelSerializer):
    """User Registration Serializer"""
    password = serializers.CharField(write_only=True)

    class Meta:
        """Class Meta"""
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.ModelSerializer):
    """Serializer for user login"""
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        """Class Meta"""
        model = User
        fields = ['username', 'password']

class MovieSerializer(serializers.ModelSerializer):
    """Movie Serializer"""
    class Meta:
        """Class Meta"""
        model = Movie
        fields = ['id', 'title', 'poster', 'genre', 'actor', 'description', 'year']
