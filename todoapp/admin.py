from ast import Add
from django.contrib import admin
from .models import Todo, AddTask
# Register your models here.
admin.site.register(Todo)
admin.site.register(AddTask)
