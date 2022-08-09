from django.urls import path
from django.http import HttpResponse
from . import views

app_name="api"
urlpatterns=[
    path('',views.index),
    ]