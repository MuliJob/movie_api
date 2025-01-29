"""View Functions"""
from django.contrib.auth.models import User
from movie.models import Movie
from movie.serializers import MovieSerializer, RegisterSerializer
from rest_framework import generics

class RegisterUser(generics.CreateAPIView):
    """Register Generic View"""
    serializer_class = RegisterSerializer


class MovieList(generics.ListCreateAPIView):
    """Listing class"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve class"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
