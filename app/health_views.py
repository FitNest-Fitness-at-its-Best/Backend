from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .models import (
    UserFoodLog
)


from .serializers import (
    UserFoodLogSerializer
)


class UserFoodLogView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserFoodLog.objects.filter(user=request.user).order_by('-added_on')
    serializer = UserFoodLogSerializer

class AddingUserFoodLogView(APIView):
    permission_classes = [IsAuthenticated]
    def image_processing(self, image):
        pass

    def post(self, request):
        image = request.FILES['food_image']
        output = self.image_processing(image)
        if output:
            return Response(output)
        else:
            return Response({
                "status": "error",
                "message": "Unable to identify object"
            }, status=404)

class EditingFoodLogView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            obj = UserFoodLog.objects.get(id=request.data.get('id')
        except Exception as e:
            print(e)
            return Response({
                "status": "error",
                "message": "No foodlog with this id"
            }, status=404)
        serializer = UserFoodLogSerializer(obj,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(edited=True)
            return Response({
                "status": "success",
                "message": "Foodlog fetched",
                "payload": serializer.data
            }, status=200)
        else:
            return Response({
                "status": "error",
                "message": serializer.errors
            }, status=400)
