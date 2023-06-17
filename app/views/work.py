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


class WorkModelForm(BootStrapModelForm):
    class Meta:
        model = models.Work
        # fields = "__all__"

        fields = ["username", "password", "time", "name", "phone", "gender"]

    def clean_phone(self):
        txt_phone = self.cleaned_data['phone']

        if len(txt_phone) != 11:
            # 验证不通过
            raise ValidationError('格式错误')

        exists_data = models.Work.objects.exclude(id=self.instance.pk).filter(phone=txt_phone).exists()
        if exists_data:
            raise ValidationError("手机号已存在")

        # 验证通过
        return txt_phone


class UserModelForm(BootStrapModelForm):
    class Meta:
        model = models.User
        # fields = "__all__"

        fields = ["username", "password"]


class Pwdform(BootStrapForm):
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


# 员工列表
def work_list(request):
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict['username__contains'] = search_data

    queryset = models.Work.objects.filter(**data_dict)

    page_object = Pagination(request, queryset, page_size=10)
    page_queryset = page_object.page_queryset

    # 调用对象的html方法,生成页码
    page_object.html()

    page_string = page_object.page_string
    head_page = page_object.head_page
    end_page = page_object.end_page

    context = {
        "work_data": page_queryset,  # 分页的数据
        "page_string": page_string,  # 页码
        "head_page": head_page,  # 首页
        "end_page": end_page,  # 尾页
    }

    return render(request, 'work_list.html', context)


# 添加新的员工信息
def work_add(request):
    if request.method == "GET":
        form = WorkModelForm()
        return render(request, 'work_add.html', {'form': form})

    form = WorkModelForm(data=request.POST)
    if form.is_valid():
        employee = form.save(commit=False)
        password = form.cleaned_data['password']
        encrypted_password = make_password(password)
        employee.password = encrypted_password
        employee.save()
        return redirect('/work/list/')
    return render(request, "work_add.html", {"form": form})


# 编辑员工信息
def work_edit(request, nid):
    row_obj = models.Work.objects.filter(id=nid).first()

    if request.method == "GET":
        form = WorkModelForm(instance=row_obj)
        return render(request, 'work_edit.html', {'form': form})

    form = WorkModelForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect("/work/list/")

    return render(request, "work_edit.html", {"form": form})


# 密码员工
def work_change(request, nid):
    row_obj = models.Work.objects.filter(id=nid).first()

    if request.method == "POST":
        form = Pwdform(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['newpassword']
            confirm_password = form.cleaned_data['newpassword2']

            if new_password != confirm_password:
                form.add_error('newpassword2', '新密码与确认密码不一致')
                return render(request, 'change_work.html', {'form': form})

            row_obj.password = make_password(new_password)
            row_obj.save()

            return redirect('/work/list/')
    else:
        form = Pwdform()

    return render(request, "work_change.html", {"form": form})


# 删除员工信息

def work_del(request, nid):
    """用户删除"""
    models.Work.objects.filter(id=nid).delete()
    return redirect("/work/list/")


# 普通用户列表
def putong_list(request):
    data = models.User.objects.all()

    page_object = Pagination(request, data, page_size=8)
    page_queryset = page_object.page_queryset

    # 调用对象的html方法,生成页码
    page_object.html()

    page_string = page_object.page_string
    head_page = page_object.head_page
    end_page = page_object.end_page

    context = {
        "putong_data": page_queryset,  # 分页的数据
        "page_string": page_string,  # 页码
        "head_page": head_page,  # 首页
        "end_page": end_page,  # 尾页
    }

    return render(request, 'putong_list.html', context)


# 编辑普通用户信息
def putong_edit(request, nid):
    row_obj = models.User.objects.filter(id=nid).first()

    if request.method == "POST":
        form = Pwdform(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['newpassword']
            confirm_password = form.cleaned_data['newpassword2']

            if new_password != confirm_password:
                form.add_error('newpassword2', '新密码与确认密码不一致')
                return render(request, 'change_work.html', {'form': form})

            row_obj.password = make_password(new_password)
            row_obj.save()

            return redirect('/putong/list/')
    else:
        form = Pwdform()

    return render(request, "putong_edit.html", {"form": form})


# 删除普通用户信息

def putong_del(request, nid):
    """用户删除"""
    models.User.objects.filter(id=nid).delete()
    return redirect("/putong/list/")
