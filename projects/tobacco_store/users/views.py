import logging
from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from .models import User

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]



class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return response

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            if not refresh_token:
                return Response({"error": "Refresh token is required."}, status=400)
            
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Вы успешно вышли"}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=400)
