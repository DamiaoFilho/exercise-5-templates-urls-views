from django.contrib import admin
from django.urls import path, include
from .views import index, login
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login')
] 