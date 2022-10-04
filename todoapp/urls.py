from django.contrib import admin
from django.urls import path
from todoapp import views

appname = 'todoapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_task/', views.add_task, name='add_task'),
    path('view_task/', views.view_task, name="view_task"),
    path('delete_task/<int:id>/', views.delete_task, name="delete_task"),
    path('update_task/<int:id>/', views.update_task, name="update_task"),
]