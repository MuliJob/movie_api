"""Movie App Urls"""
from django.urls import path

from movie import views


urlpatterns = [
    path('login/', views.LoginUser.as_view(), name="login"),
    path('register/', views.RegisterUser.as_view()),
    path('movie/', views.MovieList.as_view()),
    path('movie/<int:pk>/', views.MovieDetail.as_view()),
]
