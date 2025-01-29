from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from movie import views


urlpatterns = [
    path('auth/', obtain_auth_token),
    path('register/', views.RegisterUser.as_view()),
    path('movie/', views.MovieList.as_view()),
    path('movie/<int:pk>/', views.MovieDetail.as_view()),
]
