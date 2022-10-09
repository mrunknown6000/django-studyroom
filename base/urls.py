from django.urls import path
from django import views
from . import views

from django.urls import re_path
from django.conf import settings



urlpatterns = [
    path('', views.rootToHome),

    path('staticfiledebug/', views.staticfile),

    path('home/', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', views.staticfile),
    ]