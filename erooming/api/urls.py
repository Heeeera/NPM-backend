from django.urls import path
from .views import current_user, UserList, ProfileUpdateAPI

urlpatterns = [
    path('', UserList.as_view()),
    path('current/', current_user),
    path("auth/profile/<int:user_pk>/update/", ProfileUpdateAPI.as_view()),
]