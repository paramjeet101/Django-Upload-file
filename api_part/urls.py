"""
URL configuration for catalyst_count project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from .views import signup,login_user,upload,Alldata,users,logout_user,delete_user
from .views import QuerySetView

urlpatterns = [
    path('',signup,name="signup"),
    path('login/',login_user,name="login_user"),
    path('upload/',upload,name="upload"),
    path('builder/',Alldata,name="builder"),
    path('users/',users,name="users"),
    path('logout/',logout_user,name="logout_user"),
    path('data/',QuerySetView.as_view()),
    path('delete/<str:username>',delete_user,name="delete_user"),


]
