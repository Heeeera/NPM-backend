from django.urls import path
from django.http import HttpResponse
from . import views

app_name="api"
urlpatterns=[
    path('users/',views.users_list, name="api_users"),
    path('routine/',views.routine_list, name="api_routines"),
]