from django.urls import path
from . import views

app_name="api"
urlpatterns=[
    path('routine/',views.routine_list, name="api-routines"),
    path('routine/<int:pk>',views.routine_list_patch, name="api-routines-put"),
    path('user_routine/', views.user_routine, name="api-user-routine"),
    path('user_routine/<int:pk>', views.user_routine_patch, name="api-user-routine-put"),
    path('all_user_routines/', views.all_user_routines, name="api-personal-routine"),
    path('social_account_profile/<int:pk>', views.social_account_profile, name="api-social-account-profile"),
    path('user_routine_list/<int:pk>',views.user_routine_list, name="api-user-routine-list"),
]
