from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>', views.detail_user_todos, name='detail_user_todos'),
    path('<int:user_id>/todo/<int:todo_id>', views.detail_user_todo, name='detail_user_todo'),
]