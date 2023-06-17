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


class InModelForm(BootStrapModelForm):
    class Meta:
        model = models.RuKu
        # fields = "__all__"

        fields = ["drug_name", "in_money", "in_number", "in_time"]


# 入库记录
def ink_list(request):
    data = models.RuKu.objects.all()

    page_object = Pagination(request, data, page_size=10)
    page_queryset = page_object.page_queryset

    # 调用对象的html方法,生成页码
    page_object.html()

    page_string = page_object.page_string
    head_page = page_object.head_page
    end_page = page_object.end_page

    context = {
        "ink_data": page_queryset,  # 分页的数据
        "page_string": page_string,  # 页码
        "head_page": head_page,  # 首页
        "end_page": end_page,  # 尾页
    }

    return render(request, 'ink_list.html', context)


# 员工入库记录
def ink_worklist(request):
    data = models.RuKu.objects.all()

    page_object = Pagination(request, data, page_size=10)
    page_queryset = page_object.page_queryset

    # 调用对象的html方法,生成页码
    page_object.html()

    page_string = page_object.page_string
    head_page = page_object.head_page
    end_page = page_object.end_page

    context = {
        "ink_data": page_queryset,  # 分页的数据
        "page_string": page_string,  # 页码
        "head_page": head_page,  # 首页
        "end_page": end_page,  # 尾页
    }

    return render(request, 'ink_worklist.html', context)


# 添加新的入库记录
def ink_add(request):
    if request.method == "GET":
        form = InModelForm()
        return render(request, 'ink_add.html', {'form': form})

    form = InModelForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        ink_data = form.cleaned_data['in_number']  # 入库数量
        order_name = models.Drug.objects.filter(drugname=form.cleaned_data['drug_name'])  # 提取药品表中的数据
        # 更新数据
        for obj in order_name:
            num_value = obj.number
            new_data = num_value + ink_data
            obj.number = new_data
            obj.save()

        return redirect('/ink/list/')
    return render(request, "ink_add.html", {"form": form})



# 员工添加新的入库记录
def ink_workadd(request):
    if request.method == "GET":
        form = InModelForm()
        return render(request, 'ink_workadd.html', {'form': form})

    form = InModelForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()

        ink_data = form.cleaned_data['in_number']  # 入库数量
        order_name = models.Drug.objects.filter(drugname=form.cleaned_data['drug_name'])  # 提取药品表中的数据
        # 更新数据
        for obj in order_name:
            num_value = obj.number
            new_data = num_value + ink_data
            obj.number = new_data
            obj.save()

        return redirect('/ink/worklist/')
    return render(request, "ink_workadd.html", {"form": form})