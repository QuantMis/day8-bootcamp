# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.conf import settings
from django.conf.urls.static import static


from django.urls import path
from .views import login_view, register_user, logout_user
from django.contrib.auth.views import LogoutView
from daily_updates.views import *
from health_info.views import *
from vaccine.views import *
from premise.views import *

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", logout_user, name="logout"),

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
    path('vaccine/approve/<str:id>', vaccine_approve, name='vaccine_approve'),
    path('vaccine/delete/<str:id>', vaccine_delete, name='vaccine_delete'),



    # premise 
    path('premise_list', premise_list, name='premise_list'),
    path('premise/new', premise_new, name='premise_new'),
    path('premise/scan', mock_scan, name='mock_scan'),
    path('premise/activity', premise_activity, name='premise_activity')
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
