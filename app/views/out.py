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


class OutModelForm(BootStrapModelForm):
    class Meta:
        model = models.ChuKu
        # fields = "__all__"

        fields = ["drug_name", "out_money", "out_number", "out_time"]


# 出库记录
def out_list(request):
    data = models.ChuKu.objects.all()

    page_object = Pagination(request, data, page_size=10)
    page_queryset = page_object.page_queryset

    # 调用对象的html方法,生成页码
    page_object.html()

    page_string = page_object.page_string
    head_page = page_object.head_page
    end_page = page_object.end_page

    context = {
        "out_data": page_queryset,  # 分页的数据
        "page_string": page_string,  # 页码
        "head_page": head_page,  # 首页
        "end_page": end_page,  # 尾页
    }

    return render(request, 'out_list.html', context)

# 员工出库记录
def out_worklist(request):
    data = models.ChuKu.objects.all()

    page_object = Pagination(request, data, page_size=10)
    page_queryset = page_object.page_queryset

    # 调用对象的html方法,生成页码
    page_object.html()

    page_string = page_object.page_string
    head_page = page_object.head_page
    end_page = page_object.end_page

    context = {
        "out_data": page_queryset,  # 分页的数据
        "page_string": page_string,  # 页码
        "head_page": head_page,  # 首页
        "end_page": end_page,  # 尾页
    }

    return render(request, 'out_worklist.html', context)




# 添加新的出库记录
def out_add(request):
    if request.method == "GET":
        form = OutModelForm()
        return render(request, 'out_add.html', {'form': form})

    form = OutModelForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        out_data = form.cleaned_data['out_number']#出库数量
        order_name = models.Drug.objects.filter(drugname=form.cleaned_data['drug_name']) # 提取药品表中的数据
        # 更新数据
        for obj in order_name:
            num_value = obj.number
            new_data = num_value - out_data
            obj.number = new_data
            obj.save()

        return redirect('/out/list/')
    return render(request, "out_add.html", {"form": form})


# 员工添加新的出库记录
def out_workadd(request):
    if request.method == "GET":
        form = OutModelForm()
        return render(request, 'out_workadd.html', {'form': form})

    form = OutModelForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()


        # name = form.cleaned_data['drug_name'] #药品名称
        out_data = form.cleaned_data['out_number']#出库数量
        order_name = models.Drug.objects.filter(drugname=form.cleaned_data['drug_name']) # 提取药品表中的数据
        # 更新数据
        for obj in order_name:
            num_value = obj.number
            new_data = num_value - out_data
            obj.number = new_data
            obj.save()

        return redirect('/out/worklist/')
    return render(request, "out_workadd.html", {"form": form})
