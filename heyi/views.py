# -*- coding:utf-8 -*-
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from models import config, show

def index(request):
    tmp = get_template('index.html')
    site_info = config.objects.all()
    info_dict = {}
    for info in site_info:
        info_dict[info.name] = info.value

    site_show = show.objects.all()
    show_slide = []
    for slide in site_show:
        show_slide.append(slide.show_img)

    html = tmp.render(Context({
            'title': info_dict['site_title'],
            'site_keywords': info_dict['site_keywords'],
            'site_description': info_dict['site_description'],
            'site_logo': info_dict['site_logo'],
            'site_address': info_dict['site_address'],
            'icp': info_dict['icp'],
            'tel': info_dict['tel'],
            'fax': info_dict['fax'],
            'qq': info_dict['qq'],
            'email': info_dict['email'],
            'slide': show_slide,
        }))
    return HttpResponse(html)

def products(request):
    tmp = get_template('products.html')
    site_info = config.objects.all()
    info_dict = {}
    for info in site_info:
        info_dict[info.name] = info.value

    html = tmp.render(Context({
            'title': info_dict['site_title'],
            'site_keywords': info_dict['site_keywords'],
            'site_description': info_dict['site_description'],
            'site_logo': info_dict['site_logo'],
            'site_address': info_dict['site_address'],
            'icp': info_dict['icp'],
            'tel': info_dict['tel'],
            'fax': info_dict['fax'],
            'qq': info_dict['qq'],
            'email': info_dict['email'],
        }))
    return HttpResponse(html)

def about(request):
    tmp = get_template('about.html')
    site_info = config.objects.all()
    info_dict = {}
    for info in site_info:
        info_dict[info.name] = info.value

    html = tmp.render(Context({
            'title': info_dict['site_title'],
            'site_keywords': info_dict['site_keywords'],
            'site_description': info_dict['site_description'],
            'site_logo': info_dict['site_logo'],
            'site_address': info_dict['site_address'],
            'icp': info_dict['icp'],
            'tel': info_dict['tel'],
            'fax': info_dict['fax'],
            'qq': info_dict['qq'],
            'email': info_dict['email'],
        }))
    return HttpResponse(html)

def realview(request):
    tmp = get_template('realview.html')
    site_info = config.objects.all()
    info_dict = {}
    for info in site_info:
        info_dict[info.name] = info.value

    html = tmp.render(Context({
            'title': info_dict['site_title'],
            'site_keywords': info_dict['site_keywords'],
            'site_description': info_dict['site_description'],
            'site_logo': info_dict['site_logo'],
            'site_address': info_dict['site_address'],
            'icp': info_dict['icp'],
            'tel': info_dict['tel'],
            'fax': info_dict['fax'],
            'qq': info_dict['qq'],
            'email': info_dict['email'],
        }))
    return HttpResponse(html)

def wenhua(request):
    tmp = get_template('wenhua.html')
    site_info = config.objects.all()
    info_dict = {}
    for info in site_info:
        info_dict[info.name] = info.value

    html = tmp.render(Context({
            'title': info_dict['site_title'],
            'site_keywords': info_dict['site_keywords'],
            'site_description': info_dict['site_description'],
            'site_logo': info_dict['site_logo'],
            'site_address': info_dict['site_address'],
            'icp': info_dict['icp'],
            'tel': info_dict['tel'],
            'fax': info_dict['fax'],
            'qq': info_dict['qq'],
            'email': info_dict['email'],
        }))
    return HttpResponse(html)

def honour(request):
    tmp = get_template('honour.html')
    site_info = config.objects.all()
    info_dict = {}
    for info in site_info:
        info_dict[info.name] = info.value

    html = tmp.render(Context({
            'title': info_dict['site_title'],
            'site_keywords': info_dict['site_keywords'],
            'site_description': info_dict['site_description'],
            'site_logo': info_dict['site_logo'],
            'site_address': info_dict['site_address'],
            'icp': info_dict['icp'],
            'tel': info_dict['tel'],
            'fax': info_dict['fax'],
            'qq': info_dict['qq'],
            'email': info_dict['email'],
        }))
    return HttpResponse(html)

def contactus(request):
    tmp = get_template('contactus.html')
    site_info = config.objects.all()
    info_dict = {}
    for info in site_info:
        info_dict[info.name] = info.value

    html = tmp.render(Context({
            'title': info_dict['site_title'],
            'site_keywords': info_dict['site_keywords'],
            'site_description': info_dict['site_description'],
            'site_logo': info_dict['site_logo'],
            'site_address': info_dict['site_address'],
            'icp': info_dict['icp'],
            'tel': info_dict['tel'],
            'fax': info_dict['fax'],
            'qq': info_dict['qq'],
            'email': info_dict['email'],
        }))
    return HttpResponse(html)

def you_are_wanted(request):
    tmp = get_template('you-are-wanted.html')
    site_info = config.objects.all()
    info_dict = {}
    for info in site_info:
        info_dict[info.name] = info.value

    html = tmp.render(Context({
            'title': info_dict['site_title'],
            'site_keywords': info_dict['site_keywords'],
            'site_description': info_dict['site_description'],
            'site_logo': info_dict['site_logo'],
            'site_address': info_dict['site_address'],
            'icp': info_dict['icp'],
            'tel': info_dict['tel'],
            'fax': info_dict['fax'],
            'qq': info_dict['qq'],
            'email': info_dict['email'],
        }))
    return HttpResponse(html)
