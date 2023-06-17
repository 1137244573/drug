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




class SearchModelForm(BootStrapModelForm):
    class Meta:
        model = models.Work
        # fields = "__all__"

        fields = ["username", "password", "time", "name", "phone", "gender"]




def search_work(request):
    data_dict = {}
    search_data = request.GET.get('q', "")
    search_data_2 = request.GET.get('w', "")



    if search_data:
        data_dict['username__contains'] = search_data
    queryset = models.Work.objects.filter(**data_dict)
    if search_data_2:
        data_dict['name__contains'] = search_data_2
    queryset = models.Work.objects.filter(**data_dict)

    if not (search_data or search_data_2):
        queryset = models.Work.objects.none()


    querysets = queryset.all()

    page_object = Pagination(request, querysets, page_size=6)
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

    return render(request, 'search_work.html', context)


def search_drug(request):
    data_dict = {}
    search_data = request.GET.get('q', "")
    search_data_2 = request.GET.get('w', "")
    search_data_3 = request.GET.get('e', "")
    search_data_4 = request.GET.get('r', "")
    search_data_5 = request.GET.get('t', "")
    search_data_6 = request.GET.get('y', "")



    if search_data:
        data_dict['drugname__contains'] = search_data
    queryset = models.Drug.objects.filter(**data_dict)
    if search_data_2:
        data_dict['produce__contains'] = search_data_2
    queryset = models.Drug.objects.filter(**data_dict)

    if search_data_3:
        data_dict['drugrat__contains'] = search_data_3
    queryset = models.Drug.objects.filter(**data_dict)

    if search_data_4:
        data_dict['drugjixing__contains'] = search_data_4
    queryset = models.Drug.objects.filter(**data_dict)

    if search_data_5:
        data_dict['drugcate__contains'] = search_data_5
    queryset = models.Drug.objects.filter(**data_dict)

    if search_data_6:
        data_dict['drugnid__contains'] = search_data_6
    queryset = models.Drug.objects.filter(**data_dict)





    if not (search_data or search_data_2 or search_data_3 or search_data_4
     or search_data_5 or search_data_6):
        queryset = models.Drug.objects.none()


    querysets = queryset.all()

    page_object = Pagination(request, querysets, page_size=4)
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

    return render(request, 'search_drug.html', context)



def search_workdrug(request):
    data_dict = {}
    search_data = request.GET.get('q', "")
    search_data_2 = request.GET.get('w', "")
    search_data_3 = request.GET.get('e', "")
    search_data_4 = request.GET.get('r', "")
    search_data_5 = request.GET.get('t', "")
    search_data_6 = request.GET.get('y', "")


    if search_data:
        data_dict['drugname__contains'] = search_data
    queryset = models.Drug.objects.filter(**data_dict)
    if search_data_2:
        data_dict['produce__contains'] = search_data_2
    queryset = models.Drug.objects.filter(**data_dict)

    if search_data_3:
        data_dict['drugrat__contains'] = search_data_3
    queryset = models.Drug.objects.filter(**data_dict)

    if search_data_4:
        data_dict['drugjixing__contains'] = search_data_4
    queryset = models.Drug.objects.filter(**data_dict)

    if search_data_5:
        data_dict['drugcate__contains'] = search_data_5
    queryset = models.Drug.objects.filter(**data_dict)

    if search_data_6:
        data_dict['drugnid__contains'] = search_data_6
    queryset = models.Drug.objects.filter(**data_dict)





    if not (search_data or search_data_2 or search_data_3 or search_data_4
     or search_data_5 or search_data_6):
        queryset = models.Drug.objects.none()


    querysets = queryset.all()

    page_object = Pagination(request, querysets, page_size=4)
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

    return render(request, 'search_workdrug.html', context)



# 用户查询
def search_userdrug(request):
    data_dict = {}
    search_data = request.GET.get('q', "")
    search_data_2 = request.GET.get('w', "")
    search_data_3 = request.GET.get('e', "")
    search_data_4 = request.GET.get('r', "")
    search_data_5 = request.GET.get('t', "")
    search_data_6 = request.GET.get('y', "")


    if search_data:
        data_dict['drugname__contains'] = search_data
    queryset = models.Drug.objects.filter(**data_dict)
    if search_data_2:
        data_dict['produce__contains'] = search_data_2
    queryset = models.Drug.objects.filter(**data_dict)

    if search_data_3:
        data_dict['drugrat__contains'] = search_data_3
    queryset = models.Drug.objects.filter(**data_dict)

    if search_data_4:
        data_dict['drugjixing__contains'] = search_data_4
    queryset = models.Drug.objects.filter(**data_dict)

    if search_data_5:
        data_dict['drugcate__contains'] = search_data_5
    queryset = models.Drug.objects.filter(**data_dict)

    if search_data_6:
        data_dict['drugspe__contains'] = search_data_6
    queryset = models.Drug.objects.filter(**data_dict)





    if not (search_data or search_data_2 or search_data_3 or search_data_4
     or search_data_5 or search_data_6):
        queryset = models.Drug.objects.none()


    querysets = queryset.all()

    page_object = Pagination(request, querysets, page_size=5)
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

    return render(request, 'search_userdrug.html', context)



def search_out(request):
    data_dict = {}
    search_data = request.GET.get('q', "")
    search_data_2 = request.GET.get('w', "")
    search_data_3 = request.GET.get('e', "")
    search_data_4 = request.GET.get('r', "")
    search_data_5 = request.GET.get('t', "")
    search_data_6 = request.GET.get('y', "")



    if search_data:
        data_dict['drugname__contains'] = search_data
    queryset = models.Drug.objects.filter(**data_dict)
    if search_data_2:
        data_dict['produce__contains'] = search_data_2
    queryset = models.Drug.objects.filter(**data_dict)

    if search_data_3:
        data_dict['drugrat__contains'] = search_data_3
    queryset = models.Drug.objects.filter(**data_dict)

    if search_data_4:
        data_dict['drugnid__contains'] = search_data_4
    queryset = models.Drug.objects.filter(**data_dict)

    if search_data_5:
        data_dict['drugcate__contains'] = search_data_5
    queryset = models.Drug.objects.filter(**data_dict)
    if search_data_6:
        data_dict['drugnid__contains'] = search_data_6
    queryset = models.Drug.objects.filter(**data_dict)





    if not (search_data or search_data_2 or search_data_3 or search_data_4
     or search_data_5 or search_data_6):
        queryset = models.Drug.objects.none()


    querysets = queryset.all()

    querysetstwo = models.ChuKu.objects.filter(drug_name__in=[item.drugname for item in querysets])


    page_object = Pagination(request, querysetstwo, page_size=5)
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

    return render(request, 'search_out.html', context)


def search_workout(request):
    data_dict = {}
    search_data = request.GET.get('q', "")
    search_data_2 = request.GET.get('w', "")
    search_data_3 = request.GET.get('e', "")
    search_data_4 = request.GET.get('r', "")
    search_data_5 = request.GET.get('t', "")
    search_data_6 = request.GET.get('y', "")



    if search_data:
        data_dict['drugname__contains'] = search_data
    queryset = models.Drug.objects.filter(**data_dict)
    if search_data_2:
        data_dict['produce__contains'] = search_data_2
    queryset = models.Drug.objects.filter(**data_dict)

    if search_data_3:
        data_dict['drugrat__contains'] = search_data_3
    queryset = models.Drug.objects.filter(**data_dict)

    if search_data_4:
        data_dict['drugnid__contains'] = search_data_4
    queryset = models.Drug.objects.filter(**data_dict)

    if search_data_5:
        data_dict['drugcate__contains'] = search_data_5
    queryset = models.Drug.objects.filter(**data_dict)
    if search_data_6:
        data_dict['drugnid__contains'] = search_data_6
    queryset = models.Drug.objects.filter(**data_dict)





    if not (search_data or search_data_2 or search_data_3 or search_data_4
     or search_data_5 or search_data_6):
        queryset = models.Drug.objects.none()


    querysets = queryset.all()

    querysetstwo = models.ChuKu.objects.filter(drug_name__in=[item.drugname for item in querysets])


    page_object = Pagination(request, querysetstwo, page_size=5)
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

    return render(request, 'search_workout.html', context)



def search_in(request):
    data_dict = {}
    search_data = request.GET.get('q', "")
    search_data_2 = request.GET.get('w', "")
    search_data_3 = request.GET.get('e', "")
    search_data_4 = request.GET.get('r', "")
    search_data_5 = request.GET.get('t', "")
    search_data_6 = request.GET.get('y', "")



    if search_data:
        data_dict['drugname__contains'] = search_data
    queryset = models.Drug.objects.filter(**data_dict)
    if search_data_2:
        data_dict['produce__contains'] = search_data_2
    queryset = models.Drug.objects.filter(**data_dict)

    if search_data_3:
        data_dict['drugrat__contains'] = search_data_3
    queryset = models.Drug.objects.filter(**data_dict)

    if search_data_4:
        data_dict['drugnid__contains'] = search_data_4
    queryset = models.Drug.objects.filter(**data_dict)

    if search_data_5:
        data_dict['drugcate__contains'] = search_data_5
    queryset = models.Drug.objects.filter(**data_dict)
    if search_data_6:
        data_dict['drugnid__contains'] = search_data_6
    queryset = models.Drug.objects.filter(**data_dict)





    if not (search_data or search_data_2 or search_data_3 or search_data_4
     or search_data_5 or search_data_6):
        queryset = models.Drug.objects.none()


    querysets = queryset.all()

    querysetstwo = models.RuKu.objects.filter(drug_name__in=[item.drugname for item in querysets])


    page_object = Pagination(request, querysetstwo, page_size=5)
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

    return render(request, 'search_in.html', context)




def search_workin(request):
    data_dict = {}
    search_data = request.GET.get('q', "")
    search_data_2 = request.GET.get('w', "")
    search_data_3 = request.GET.get('e', "")
    search_data_4 = request.GET.get('r', "")
    search_data_5 = request.GET.get('t', "")
    search_data_6 = request.GET.get('y', "")



    if search_data:
        data_dict['drugname__contains'] = search_data
    queryset = models.Drug.objects.filter(**data_dict)
    if search_data_2:
        data_dict['produce__contains'] = search_data_2
    queryset = models.Drug.objects.filter(**data_dict)

    if search_data_3:
        data_dict['drugrat__contains'] = search_data_3
    queryset = models.Drug.objects.filter(**data_dict)

    if search_data_4:
        data_dict['drugnid__contains'] = search_data_4
    queryset = models.Drug.objects.filter(**data_dict)

    if search_data_5:
        data_dict['drugcate__contains'] = search_data_5
    queryset = models.Drug.objects.filter(**data_dict)
    if search_data_6:
        data_dict['drugnid__contains'] = search_data_6
    queryset = models.Drug.objects.filter(**data_dict)





    if not (search_data or search_data_2 or search_data_3 or search_data_4
     or search_data_5 or search_data_6):
        queryset = models.Drug.objects.none()


    querysets = queryset.all()

    querysetstwo = models.RuKu.objects.filter(drug_name__in=[item.drugname for item in querysets])


    page_object = Pagination(request, querysetstwo, page_size=5)
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

    return render(request, 'search_workin.html', context)