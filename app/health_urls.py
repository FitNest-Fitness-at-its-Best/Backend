from django.urls import path, include
from rest_framework import routers
from . import health_views
router = routers.DefaultRouter()


urlpatterns = [
    path('prediction/', health_views.AddingUserFoodLogView.as_view()),
]
