import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import User, Todo
from .serializers import UserSerializers, TodoSerializers
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.


def index(request):
    allUsers = User.objects.all()
    data = UserSerializers(allUsers, many=True)
    return JsonResponse(data.data, safe=False, status=status.HTTP_200_OK)


def detail_user_todos(request, user_id):
    todos = Todo.objects.get(user=user_id)
    data = TodoSerializers(todos, many=True)
    response = " you are looking all the todo of the user with id: %s" % user_id
    return JsonResponse(data.data, safe=False, status=status.HTTP_200_OK)


def detail_user_todo(request, user_id, todo_id):
    response = f"you are seeking the todo id : {todo_id} of the user {user_id}"
    return HttpResponse(response)


@csrf_exempt
def create_user(request):
    user_from_form = JSONParser().parse(request)
    finalizeUser = UserSerializers(data=user_from_form)
    try:
        if finalizeUser.is_valid():
            name = user_from_form.get("name")
            surname = user_from_form.get("surname")
            password = make_password(user_from_form.get("password"))
            email = user_from_form.get("email")
            user = User( name=name, surname=surname, password=password, email=email)
            user.save()

            final = UserSerializers(user, many=False)
            return JsonResponse({'message': 'User saved Successfully', 'savedUser': final.data}, safe=False,
                                status=status.HTTP_200_OK)
        response = "Sorry ! We can not process your request with empty values"
        return JsonResponse({'message': response}, safe=False, status=status.HTTP_401_UNAUTHORIZED)
    except ValueError as err:
        return JsonResponse({'message': f"{err.__str__()}"}, safe=False, status=status.HTTP_401_UNAUTHORIZED)


def create_todo(request, user_id):
    response = f"you want to create a todo for the user {user_id}"
    return HttpResponse(response)


def update_user_informations(request, user_id):
    response = f"you want to update the informations fo the user {user_id}"
    return HttpResponse(response)


def update_user_todo(request, user_id, todo_id):
    response = f"you want to update the todo id: {todo_id} of the user with ID:{user_id}"
    return HttpResponse(response)
