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


class DrugModelForm(BootStrapModelForm):
    class Meta:
        model = models.Drug
        # fields = "__all__"

        fields = ["drugname", "drugjixing", "drugcate", "money", "number", "drugspe",
                  "produce", "insure", "drugrat", "drugnid", "drugun", "drugkey", "drugant"]



# 药品列表
def drug_list(request):
    data = models.Drug.objects.all()

    page_object = Pagination(request, data, page_size=8)
    page_queryset = page_object.page_queryset

    # 调用对象的html方法,生成页码
    page_object.html()

    page_string = page_object.page_string
    head_page = page_object.head_page
    end_page = page_object.end_page

    context = {
        "drug_data": page_queryset,  # 分页的数据
        "page_string": page_string,  # 页码
        "head_page": head_page,  # 首页
        "end_page": end_page,  # 尾页
    }

    return render(request, 'drug_list.html', context)


# 员工药品列表
def drug_worklist(request):
    data = models.Drug.objects.all()

    page_object = Pagination(request, data, page_size=8)
    page_queryset = page_object.page_queryset

    # 调用对象的html方法,生成页码
    page_object.html()

    page_string = page_object.page_string
    head_page = page_object.head_page
    end_page = page_object.end_page

    context = {
        "drug_data": page_queryset,  # 分页的数据
        "page_string": page_string,  # 页码
        "head_page": head_page,  # 首页
        "end_page": end_page,  # 尾页
    }

    return render(request, 'drug_worklist.html', context)


# 用户药品列表
def drug_userlist(request):
    data = models.Drug.objects.all()

    page_object = Pagination(request, data, page_size=8)
    page_queryset = page_object.page_queryset

    # 调用对象的html方法,生成页码
    page_object.html()

    page_string = page_object.page_string
    head_page = page_object.head_page
    end_page = page_object.end_page

    context = {
        "drug_data": page_queryset,  # 分页的数据
        "page_string": page_string,  # 页码
        "head_page": head_page,  # 首页
        "end_page": end_page,  # 尾页
    }

    return render(request, 'drug_userlist.html', context)



# 员工添加药品
def drug_workadd(request):
    if request.method == "GET":
        form = DrugModelForm()
        return render(request, 'drug_workadd.html', {'form': form})

    form = DrugModelForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return redirect('/drug/worklist/')
    return render(request, "drug_workadd.html", {"form": form})


# 添加新的药品
def drug_add(request):
    if request.method == "GET":
        form = DrugModelForm()
        return render(request, 'drug_add.html', {'form': form})

    form = DrugModelForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return redirect('/drug/list/')
    return render(request, "drug_add.html", {"form": form})


# 编辑药品信息
def drug_edit(request, nid):
    row_obj = models.Drug.objects.filter(id=nid).first()

    if request.method == "GET":
        form = DrugModelForm(instance=row_obj)
        return render(request, 'drug_edit.html', {'form': form})

    form = DrugModelForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect("/drug/list/")

    return render(request, "drug_edit.html", {"form": form})


# 员工编辑药品信息
def drug_workedit(request, nid):
    row_obj = models.Drug.objects.filter(id=nid).first()

    if request.method == "GET":
        form = DrugModelForm(instance=row_obj)
        return render(request, 'drug_workedit.html', {'form': form})

    form = DrugModelForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect("/drug/worklist/")

    return render(request, "drug_workedit.html", {"form": form})


# 删除药品信息

def drug_del(request, nid):
    """用户删除"""
    models.Drug.objects.filter(id=nid).delete()
    return redirect("/drug/list/")


# 删除药品信息

def drug_workdel(request, nid):
    """用户删除"""
    models.Drug.objects.filter(id=nid).delete()
    return redirect("/drug/worklist/")


# 药品数量较少
def stock_query(request):
    drugs = models.Drug.objects.filter(number__lt=80)
    if drugs.exists():
        messages = [{'name': drug.drugname, 'number': drug.number} for drug in drugs]
        return render(request, 'stock_query.html', {'messages': messages})
    else:
        return render(request, 'stock_query.html', {'empty_message': True})


def stock_querywork(request):
    drugs = models.Drug.objects.filter(number__lt=80)
    if drugs.exists():
        messages = [{'name': drug.drugname, 'number': drug.number} for drug in drugs]
        return render(request, 'stock_querywork.html', {'messages': messages})
    else:
        return render(request, 'stock_querywork.html', {'empty_message': True})
