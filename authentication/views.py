# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib.auth import get_user_model

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
#from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm
from user.models import CustomUser
from health_info.models import HealthInformation


def login_view(request):

    User = get_user_model()
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                # check if user have info 
                # dont have one
                # create for the user
                user = CustomUser.objects.filter(email = request.user)[0]
                hi = HealthInformation.objects.filter(user = user)
                if len(hi) == 0:

                    hi = HealthInformation.objects.create()
                    hi.user = user
                    hi.save()

                return redirect('daily_updates')

            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "accounts/login.html", {"form": form, "msg" : msg})

def register_user(request):

    User = get_user_model()

    msg     = None
    success = False

    if request.method == "POST":
        print(request.POST)
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg     = 'User created - please <a href="/login">login</a>.'
            success = True
            
            
            return redirect("login")

        else:
            print("bbbb")
            msg = 'Form is not valid'    
    else:
        print("ccccc")
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg" : msg, "success" : success })
