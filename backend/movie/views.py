"""View Functions"""
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse

from movie.models import Movie

from movie.serializers import LoginSerializer, MovieSerializer, RegisterSerializer

from rest_framework.authtoken.models import Token
from rest_framework import authentication, generics, status, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .auth import TokenAuthentication

class IsNotAuthenticated(permissions.BasePermission):
    """Custom permission to prevent logged-in users from accessing the view"""

    def has_permission(self, request, view):
        """Allow only unauthenticated users"""
        return not request.user.is_authenticated

class RegisterUser(generics.CreateAPIView):
    """User Registration View"""
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsNotAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        token = Token.objects.get_or_create(user=user)

        login_url = reverse('login')

        return Response({
            "message": "User registered successfully. Please log in.",
            "redirect_to": request.build_absolute_uri(login_url),
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            },
            "token": token.key
        }, status=status.HTTP_201_CREATED)

class LoginUser(generics.GenericAPIView):
    """Logs in a user, creates a session, and returns a new authentication token"""
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        """Logs in a user, creates a session, and returns a new authentication token"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)

            return Response({
                "message": "Login successful",
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
    authentication_classes = [
        authentication.SessionAuthentication, 
        TokenAuthentication]
    permission_classes = [IsAuthenticated]


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve class"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [
        authentication.SessionAuthentication, 
        TokenAuthentication]
    permission_classes = [IsAuthenticated]
