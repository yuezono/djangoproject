"""django_app URL Configuration
...
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('memo_app.urls')),
]