from google.auth.transport import requests
from google.oauth2 import id_token

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.conf import settings

from rest_framework import status
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import User, Question, Answer


class GoogleSignInView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        client_id = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY

        try:
            idinfo = id_token.verify_oauth2_token(request.data['id_token'], requests.Request(), client_id)
        except Exception as error:
            print(error)
            return Response({"message": "Something went wrong"}, status=status.HTTP_403_FORBIDDEN)
        # print(idinfo['email'])
        # print(idinfo['name'])

        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')

        try:
            user = User.objects.get(email=idinfo['email'])
        except User.DoesNotExist:
            user = User()
            user.username = idinfo['name']
            user.email = idinfo['email']
            user.password = make_password(BaseUserManager().make_random_password())
            user.profile_image = idinfo['picture']
            user.save()
            
        token, _ = Token.objects.get_or_create(user=user)
        response = {
            'message': 'User Logged In',
            'User': {
                'id':user.id,
                'username': user.username,
                'email': user.email,
                'profile_image': user.profile_image
            },
            'token': token.key
        }
        return Response(response, status=status.HTTP_200_OK)


# Signout new user
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        user = request.user
        response = {
            "message":"User logged out", 
            "Details":{
                "id": user.id,
                "email":user.email,
                "username":user.username
            }}
        request.user.auth_token.delete()
        return Response(response, status=status.HTTP_200_OK)
        