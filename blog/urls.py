from django.urls import path
from . import viewss

urlpatterns = [
    path('', views.post_list, name='post_list'),
]