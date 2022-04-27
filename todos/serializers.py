from rest_framework import serializers
from .models import User, Todo


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'surname', 'email')


class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'is_done', 'user')


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=("email", "password")