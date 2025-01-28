"""Movie Serializers"""
from rest_framework import serializers

from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    """Movie Serializer"""
    class Meta:
        """Class Meta"""
        model = Movie
        fields = ['id', 'title', 'poster', 'genre', 'actor', 'description', 'year']
