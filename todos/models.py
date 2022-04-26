from django.db import models

# Create your models here.


class User(models.Model):
    name=models.CharField(max_length=200)
    surname=models.CharField(max_length=200)
    email=models.CharField(max_length=40)
    password=models.CharField(max_length=200)

class Todo(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    is_done=models.BooleanField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)