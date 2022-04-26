import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import User, Todo
from .serializers import UserSerializers
from rest_framework import status

# Create your views here.


def index(request):
    allUsers = User.objects.all()
    data = UserSerializers(allUsers, many=True)
    return JsonResponse(data.data,safe=False,status=status.HTTP_200_OK)


def detail_user_todos(request, user_id):
    response = " you are looking all the todo of the user with id: %s" % user_id
    return HttpResponse(response)


def detail_user_todo(request, user_id, todo_id):
    response = f"you are seeking the todo id : {todo_id} of the user {user_id}"
    return HttpResponse(response)


def create_user(request):
    response = " You wan to create a user"
    return HttpResponse(response)


def create_todo(request, user_id):
    response = f"you want to create a todo for the user {user_id}"
    return HttpResponse(response)


def update_user_informations(request, user_id):
    response = f"you want to update the informations fo the user {user_id}"
    return HttpResponse(response)


def update_user_todo(request, user_id, todo_id):
    response = f"you want to update the todo id: {todo_id} of the user with ID:{user_id}"
    return HttpResponse(response)