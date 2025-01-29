"""Movie Serializers"""
from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Movie

class RegisterSerializer(serializers.ModelSerializer):
    """User Registration"""
    class Meta:
        """Registration Fields"""
        model = User
        fields = ['id', 'username', 'password']

class MovieSerializer(serializers.ModelSerializer):
    """Movie Serializer"""
    class Meta:
        """Class Meta"""
        model = Movie
        fields = ['id', 'title', 'poster', 'genre', 'actor', 'description', 'year']
