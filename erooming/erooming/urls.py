from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import routers
from api.views import UserViewSet

router = routers.DefaultRouter()
router.register('user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include('dj_rest_auth.registration.urls')),
    path('api/', include('dj_rest_auth.urls')),
    path('api/', include('allauth.urls')),
    path('api/', include('api.urls')),
]