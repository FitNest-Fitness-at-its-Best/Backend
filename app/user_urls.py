from django.urls import path, include
from .views import (
    GoogleSignInView,
    LogoutView,
)
from rest_framework import routers

router = routers.DefaultRouter()


urlpatterns = [
    path("login/", GoogleSignInView.as_view()),
    path("logout/", LogoutView.as_view()),
]
