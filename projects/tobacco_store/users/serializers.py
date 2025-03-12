from rest_framework import serializers
from django.contrib.auth import get_user_model

user = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ["id", "username", "email", "phone"]



from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        username = attrs.get("username") or attrs.get("email")  # Поддержка email
        attrs["username"] = username  # Приводим к username, чтобы избежать ошибки
        return super().validate(attrs)
