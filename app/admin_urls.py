from django.urls import path, include

from .admin_views import (
    AdminSignupView,
    AdminLoginView,
    AdminLogoutView,
)


from rest_framework import routers

router = routers.DefaultRouter()


urlpatterns = [
    path("signup/", AdminSignupView.as_view()),
    path("login/", AdminLoginView.as_view()),
    path("logout/", AdminLogoutView.as_view()),
]
