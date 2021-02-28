import os

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.contrib.auth import authenticate, login, logout

from .models import User

# View for Admin Signup
class AdminSignupView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        if (request.data.get('password', None)==os.getenv('ADMIN_PASSWORD') and 
            request.data.get('username', None)==os.getenv('ADMIN_USERNAME') and 
            request.data.get('email', None)==os.getenv('ADMIN_EMAIL_ID')):

            try:
                user = User.objects.get(email=request.data['email'])
                return Response({"message":"Admin already signed Up"}, status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                User.objects.create_superuser(
                    email=request.data['email'],
                    username=request.data['username'],
                    password=request.data['password'],
                    profile_image=None
                )
                user = User.objects.get(email=request.data['email'])
                return Response({"message":"Admin Signed up"}, status=status.HTTP_200_OK)

        else:            
            return Response({"message":"Invalid Email and Password"}, status=status.HTTP_400_BAD_REQUEST)

class AdminLoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        user = authenticate(email=request.data.get('email', None), password=request.data.get('password',None))

        if not user:
            return Response({"message":"Invalid Details"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            if user.is_superuser:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({"message":"Admin Logged In", "token":token.key})
            else:
                return Response({"message":"Not an Admin"}, status=status.HTTP_400_BAD_REQUEST)


class AdminLogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        response = {"message":"Admin logged out"}
        request.user.auth_token.delete()
        return Response(response, status=status.HTTP_200_OK)

