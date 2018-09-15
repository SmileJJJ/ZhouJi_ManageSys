from django.http import HttpResponse
from django.shortcuts import render
from .models import *

import json

# Create your views here.
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
