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

def get_mysqlData(table_name):
    target_list = models_list[table_name].objects.all()
    target_list_json = serializers.serialize('json', target_list)
    target_list = json.loads(target_list_json)
    target_list_json = []
    for i in target_list:
        dic = i['fields']
        dic['id'] = i['pk']
        target_list_json.append(dic)
    print (target_list_json)
    with open('./static/data/data.json', 'w') as f:
        f.write(json.dumps(target_list_json))

# Create your views here.
def login_views(request):
    return render(request,'login.html')

def index_views(request):
    get_mysqlData('company_member')
    return render(request,'index.html')

def customer_info_views(request):
    get_mysqlData('customer_info')
    return render(request, 'customer_info.html')












def check_login_views(request):
    name = request.POST['login']
    pwd = request.POST['pwd']
    ulist = company_member.objects.filter(name=name,password=pwd)
    if ulist:
        dic = {'status':1}
    else:
        dic = {'status':0}
    return HttpResponse(json.dumps(dic))













# def get_info_views(request):
#     target = request.GET['target']
#     target_list = models_list[target].objects.all()
#     target_list_json = serializers.serialize('json',target_list)
#     target_list = json.loads(target_list_json)
#     target_list_json = []
#     fields_list = ['id','name','gender','introduce']
#     for i in target_list:
#         dic = i['fields']
#         dic['id'] = i['pk']
#         target_list_json.append(dic)
#     with open('./static/data/data.json','w') as f:
#         f.write(json.dumps(target_list_json))
#     return HttpResponse(json.dumps(fields_list))
