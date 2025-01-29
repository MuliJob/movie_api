"""View Functions"""
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from movie.models import Movie

from movie.serializers import LoginSerializer, MovieSerializer, RegisterSerializer

from rest_framework.authtoken.models import Token
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .auth import TokenAuthentication


class RegisterUser(generics.CreateAPIView):
    """Register Generic View"""
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginUser(generics.GenericAPIView):
    """Logs in a user and returns a new authentication token"""
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        """User Login"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]

        user = authenticate(username=username, password=password)

        if user:
            # Delete old token (if exists) and create a new one
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)

            return Response({
                "token": token.key,
                "user": {
                    "id": user.id,
                    "username": user.username
                }
            }, status=status.HTTP_200_OK)

        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class MovieList(generics.ListCreateAPIView):
    """Listing class"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [TokenAuthentication]  # Require token authentication
    permission_classes = [IsAuthenticated]


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve class"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [TokenAuthentication]  # Require token authentication
    permission_classes = [IsAuthenticated]
