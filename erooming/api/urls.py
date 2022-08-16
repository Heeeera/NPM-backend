from django.urls import path
from django.http import HttpResponse
from . import views

app_name="api"
urlpatterns=[
    path('users/',views.users_list, name="api-users"),
    path('routine/',views.routine_list, name="api-routines"),
    path('routine/<int:pk>',views.routine_list_put, name="api-routines-put"),
    path('user_routine/', views.user_routine, name="api-user-routine"),
    path('user_routine/<int:pk>', views.user_routine_put, name="api-user-routine-put"),
]
