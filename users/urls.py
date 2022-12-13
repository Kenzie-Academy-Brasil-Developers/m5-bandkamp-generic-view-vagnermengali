from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("users/", views.CreateAPIView.as_view()),
    path("users/<int:pk>/", views.RetrieveUpdateDestroyAPIView.as_view()),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
]
