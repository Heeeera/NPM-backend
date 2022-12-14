"""erooming URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from social_login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls'), name="api"),
    path('dj-rest-auth/google/', views.GoogleLogin.as_view(), name='google_login'),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    re_path(r'^accounts/', include('allauth.urls'), name='socialaccount_signup'),
]
