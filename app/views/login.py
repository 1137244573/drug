import json
from django.shortcuts import render, redirect, HttpResponse
from app import models
from django import forms
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.safestring import mark_safe
from app.utils.pagination import Pagination
from app.utils.bootstrap import BootStrapModelForm, BootStrapForm
from datetime import datetime
from random import randint
from django.contrib.auth.hashers import make_password, check_password



class LoginForm(BootStrapForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput,
        required=True,
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput,
        required=True,
    )

class Pwdform(BootStrapForm):
    oldpassword = forms.CharField(
        label="旧密码",
        widget=forms.TextInput,
        required=True,
    )
    newpassword = forms.CharField(
        label="新密码",
        widget=forms.TextInput,
        required=True,
    )
    newpassword2 = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput,
        required=True,
    )


shenfen = None


# 登录
def login(request):
    """管理员登录"""
    global shenfen
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {"form": form})

    form = LoginForm(data=request.POST)
    ident = request.POST.get('ident')
    if ident == 'admin':
        if form.is_valid():
            # 去数据库校验用户名和密码是否正确
            admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
            # 如果数据库中没有查询到数据
            if not admin_object:
                form.add_error("password", "用户名或密码错误")
                return render(request, 'login.html', {"form": form})

            request.session['info'] = {'id': admin_object.id, 'name': admin_object.username}

            return redirect('/home/')

    if ident == 'work':   # 员工登录
        if form.is_valid():
            # 去数据库校验用户名和密码是否正确
            work_object = models.Work.objects.filter(username=form.cleaned_data['username']).first()
            # 如果数据库中没有查询到数据
            if not work_object or not check_password(form.cleaned_data['password'], work_object.password):
                form.add_error("password", "用户名或密码错误")
                return render(request, 'login.html', {"form": form})

            request.session['info'] = {'id': work_object.id, 'name': work_object.name}
            shenfen = form.cleaned_data['username']
            return redirect('/home_2/')

    if ident == 'user':   # 普通用户登录
        if form.is_valid():
            # 去数据库校验用户名和密码是否正确
            user_object = models.User.objects.filter(username=form.cleaned_data['username']).first()
            # 如果数据库中没有查询到数据
            if not user_object or not check_password(form.cleaned_data['password'], user_object.password):
                form.add_error("password", "用户名或密码错误")
                return render(request, 'login.html', {"form": form})

            request.session['info'] = {'id': user_object.id, 'name': user_object.username}
            shenfen = form.cleaned_data['username']
            return redirect('/home_3/')

    return render(request, 'login.html', {"form": form})

# 注销
def logout(request):
    request.session.clear()

    return redirect('/login/')


# 注册

def login_reg(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login_reg.html', {'form': form})


    elif request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username_data = form.cleaned_data['username']
            password_data = form.cleaned_data['password']

            # 密码加密
            en_password = make_password(password_data)

            models.User.objects.create(username=username_data, password=en_password)

            return redirect('/login/')
    return render(request, "login_reg.html", {"form": form})

# 用户密码修改
def change_pwd(request):
    global shenfen
    user_object = models.User.objects.filter(username=shenfen).first()
    if request.method == "POST":
        form = Pwdform(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data['oldpassword']
            new_password = form.cleaned_data['newpassword']
            confirm_password = form.cleaned_data['newpassword2']

            if check_password(old_password, user_object.password) is False:
                form.add_error('oldpassword', '旧密码输入错误')
                return render(request, 'change.html', {'form': form})

            if new_password != confirm_password:
                form.add_error('newpassword2', '新密码与确认密码不一致')
                return render(request, 'change.html', {'form': form})

            user_object.password = make_password(new_password)
            user_object.save()

            return redirect('/home_3/')
    else:
        form = Pwdform()

    return render(request, 'change.html', {'form': form})


# 员工密码修改

def change_workpwd(request):
    global shenfen
    user_object = models.Work.objects.filter(username=shenfen).first()
    if request.method == "POST":
        form = Pwdform(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data['oldpassword']
            new_password = form.cleaned_data['newpassword']
            confirm_password = form.cleaned_data['newpassword2']

            if check_password(old_password, user_object.password) is False:
                form.add_error('oldpassword', '旧密码输入错误')
                return render(request, 'change.html', {'form': form})

            if new_password != confirm_password:
                form.add_error('newpassword2', '新密码与确认密码不一致')
                return render(request, 'change_work.html', {'form': form})

            user_object.password = make_password(new_password)
            user_object.save()

            return redirect('/home_2/')
    else:
        form = Pwdform()

    return render(request, 'change_work.html', {'form': form})
