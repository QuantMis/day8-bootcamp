# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from authentication.views import login_view

from daily_updates.views import *

urlpatterns = [

    path('', login_view, name='login'),
    re_path(r'^.*\.*', views.pages, name='pages'),

    # daily updates

    path('daily-updates/', daily_updates_list, name='daily_updates'),
    path('daily-updates/new/', daily_updates_new, name='daily_updates_new'),



]
