import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import User, Todo
from .serializers import UserSerializers, TodoSerializers, LoginSerializer
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET'])
def index(request):
    allUsers = User.objects.all()
    data = UserSerializers(allUsers, many=True)
    return JsonResponse(data.data, safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
def detail_user_todos(request, user_id):
    """Get the todos of the user with the ID : <user_id>"""
    try:
        user = User.objects.get(pk=user_id)
        todos = Todo.objects.all().filter(user=user)
        data = TodoSerializers(todos, many=True)
        return JsonResponse(data.data, safe=False, status=status.HTTP_200_OK)
    except Exception as err:
        return JsonResponse({'message': f"{err.__str__()}"}, safe=False, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def detail_user_todo(request, user_id, todo_id):
    """Get the task detail with ID: <todo_id> of the user with ID: <user_id>"""
    try:
        user = User.objects.get(pk=user_id)
        todo_formatted = Todo.objects.filter(user=user)[0]
        data = TodoSerializers(todo_formatted)
        return JsonResponse(data.data, safe=False,status=status.HTTP_200_OK)
    except Exception as err:
        return JsonResponse({'message': f"{err.__str__()}"}, safe=False, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def create_user(request):
    """For Creating a User"""
    user_from_form = JSONParser().parse(request)
    finalizeUser = UserSerializers(data=user_from_form)
    try:
        if finalizeUser.is_valid():
            name = user_from_form.get("name")
            surname = user_from_form.get("surname")
            password = make_password(user_from_form.get("password"))
            email = user_from_form.get("email")
            user = User(name=name, surname=surname, password=password, email=email)
            user.save()

            final = UserSerializers(user, many=False)
            return JsonResponse({'message': 'User saved Successfully', 'savedUser': final.data}, safe=False,
                                status=status.HTTP_200_OK)
        response = "Sorry ! We can not process your request with empty values"
        return JsonResponse({'message': response}, safe=False, status=status.HTTP_401_UNAUTHORIZED)
    except ValueError as err:
        return JsonResponse({'message': f"{err.__str__()}"}, safe=False, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def create_todo(request, user_id):
    """For Creating a task for the user with id <user_id>"""
    try:
        user = User.objects.get(pk=user_id)
        if user.id is not None:
            todo_from_form = JSONParser().parse(request)
            todo_serialized = TodoSerializers(data=todo_from_form)
            if todo_serialized.is_valid():
                title = todo_from_form.get("title")
                description = todo_from_form.get("description")
                is_done = todo_from_form.get("is_done")
                todo = Todo(title=title, description=description, is_done=is_done, user=user)
                todo.save()

                response = TodoSerializers(todo, many=False)
                return JsonResponse({'message': 'Todo saved Successfully', 'savedUser': response.data}, safe=False,
                                    status=status.HTTP_200_OK)
            response = "Sorry ! We can not process your request with empty values"
            return JsonResponse({'message': response}, safe=False, status=status.HTTP_401_UNAUTHORIZED)
        else:
            response = f"Sorry ! We can not process your request , the user with ID: {user_id} does not exist"
            return JsonResponse({'message': response}, safe=False, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as err:
        return JsonResponse({'message': f"{err.__str__()}"}, safe=False, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def login_user(request):
    form_parsed = JSONParser().parse(request)
    print(form_parsed)
    response = f"you want to login the user"
    return HttpResponse(response)


def update_user_informations(request, user_id):
    response = f"you want to update the informations fo the user {user_id}"
    return HttpResponse(response)


def update_user_todo(request, user_id, todo_id):
    response = f"you want to update the todo id: {todo_id} of the user with ID:{user_id}"
    return HttpResponse(response)
