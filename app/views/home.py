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



def home(request):

    return render(request, 'home.html')

def home_2(request):

    return render(request, 'home_2.html')

def home_3(request):

    return render(request, 'home_3.html')






