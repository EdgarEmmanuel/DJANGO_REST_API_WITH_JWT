from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/user', views.create_user, name="create_user"),
    path('<int:user_id>/create/todo', views.create_todo, name="create_todo"),

    path('update/<int:user_id>', views.update_user_informations, name="update_user_informations"),
    path('<int:user_id>/update/todo/<int:todo_id>', views.update_user_todo, name="update_user_todo"),

    path('<int:user_id>', views.detail_user_todos, name='detail_user_todos'),
    path('<int:user_id>/todo/<int:todo_id>', views.detail_user_todo, name='detail_user_todo'),
]