from django.urls import path
from . import views

app_name="api"
urlpatterns=[
    path('routine/',views.routine_list, name="api-routines"),
    path('routine/<int:pk>',views.routine_list_patch, name="api-routines-put"),
    path('user_routine/', views.user_routine, name="api-user-routine"),
    path('user_routine/<int:pk>', views.user_routine_patch, name="api-user-routine-put"),
]
