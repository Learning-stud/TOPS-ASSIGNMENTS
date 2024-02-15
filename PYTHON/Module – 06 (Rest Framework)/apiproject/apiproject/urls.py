# apiproject/urls.py
from django.contrib import admin
from django.urls import path, include
# import apiapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apiapp.urls')),
]