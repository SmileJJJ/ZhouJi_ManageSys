from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from .models import *

import json

models_list = {
               'company_member':company_member,
               'customer_info':customer_info,
               'supplier_info':supplier_info,
               'factory_info':factory_info,
               }

def login_views(request):
    return render(request,'login.html')

def index_views(request):
    return render(request,'index.html')

def check_login_views(request):
    name = request.POST['login']
    pwd = request.POST['pwd']
    ulist = company_member.objects.filter(name=name,password=pwd)
    if ulist:
        dic = {'status':1}
    else:
        dic = {'status':0}
    return HttpResponse(json.dumps(dic))

def get_info_views(request):
    target = request.GET['target']
    target_list = models_list[target].objects.all()
    target_list_json = serializers.serialize('json',target_list)
    return HttpResponse(target_list_json)
