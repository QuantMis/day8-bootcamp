# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView
from daily_updates.views import *
from health_info.views import *
from vaccine.views import *


urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),

    # daily updates
    path('daily-updates/', daily_updates_list, name='daily_updates'),
    path('daily-updates/new/', daily_updates_new, name='daily_updates_new'),
    path('daily-updates/update/<str:pk>', daily_updates_update, name='daily_updates_update'),

    # health information
    path('health-info/', health_info_list, name='health_info'),
    path('health-info/new/<str:pk>', health_info_update, name='health_info_new'),

    # vaccine
    path('vaccine_list', vaccine_list, name='vaccine_list'),
    path('vaccine/new/', vaccine_new, name='vaccine_new'),



    
    
]
