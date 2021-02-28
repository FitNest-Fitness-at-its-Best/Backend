from rest_framework import serializers
from .models import  User, UserFoodLog



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'profile_image', 'date_joined')


class UserFoodLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFoodLog
        exclude = ["user"]