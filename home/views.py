# -*- coding:utf-8 -*-
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime

def index(request):
    tmp = get_template('index.html')
    html = tmp.render(Context({'title': '合一体育'}))
    return HttpResponse(html)
