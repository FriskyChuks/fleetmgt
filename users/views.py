from django.shortcuts import render

# Create your views here.
from django import template
from django.shortcuts import render

# Create your views here.
# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm


def home_view(request):

    template = 'home.html'
    context = {}
    return render(request, template, context)


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("/home")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Wrong login credentials!'    

    return render(request, "users/login.html", {"form": form, "msg" : msg})



def register_user(request):

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(email=email, password=raw_password)

            msg     = 'User created - please <a href="/">login</a>.'
            success = True
            
            #return redirect("/login/")

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "users/register.html", {"form": form, "msg" : msg, "success" : success })


def table(request):
    template = "tables.html"
    context = {}
    return render(request, template, context)
