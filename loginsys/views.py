# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from loginsys.forms import *


def login(request):
    args = {}
    args['form'] = LoginForm()
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        #login_form = LoginForm(request.POST)
        user = authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Пользователь не найден"
            return render(request, 'pageLogin.html', args)

    else:
        return render(request, 'pageLogin.html', args)


def logout(request):
    auth.logout(request)
    return redirect("/")


def register(request):
    args = {}
    args['form'] = RegForm()
    if request.method == 'POST':
        newuser_form = RegForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            # newuser = auth.authenticate(email=newuser_form.cleaned_data['email'], password=newuser_form.cleaned_data['password2'])
            # auth.login(request, newuser)
            return redirect('/auth/login')
        else:
            args['form'] = newuser_form
    return render(request, 'register.html', args)
