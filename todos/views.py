from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse("Hello world")


def detail_user_todos(request, user_id):
    response = " you are looking all the todo of the user with id: %s" % user_id
    return HttpResponse(response)


def detail_user_todo(request, user_id, todo_id):
    response = f"you are seeking the todo id : {todo_id} of the user {user_id}"
    return HttpResponse(response)
