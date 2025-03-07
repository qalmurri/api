from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import User
from .serializers import UserSerializer, RegisterSerializer

class UserList(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

class UserRegister(APIView):
    def get(self, request):
        user = User.objects.all().order_by('-id')[:2]
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
