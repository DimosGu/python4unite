# -*- coding:utf-8 -*-
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from python4unite.settings import SITE_ROOT
from models import config, show, page, product, product_category
from common import info_dict, show_slide

def index(request):
    tmp = get_template('index.html')

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

def product_cate(request):
    tmp = get_template('product_cate.html')

    product_set = product.objects.all()
    product_list = []
    for single_product in product_set:
        item = {}
        item['product_name']    = single_product.product_name
        item['price']           = 0.00
        item['product_image']   = single_product.product_image
        item['content']         = single_product.content
        item['keywords']        = single_product.keywords
        item['description']     = single_product.description
        product_list.append(item)
    pass

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
            'products':product_list,
        }))
    return HttpResponse(html)

def contactus(request):
    tmp = get_template('contactus.html')

    html = tmp.render(Context({
            'name': info_dict['site_name'],
            'title': u'联系我们 | ' + info_dict['site_name'],
            'site_keywords': info_dict['site_keywords'],
            'site_description': info_dict['site_description'],
            'site_logo': info_dict['site_logo'],
            'site_address': info_dict['site_address'],
            'icp': info_dict['icp'],
            'tel': info_dict['tel'],
            'fax': info_dict['fax'],
            'qq': info_dict['qq'],
            'email': info_dict['email'],
            'site_root': SITE_ROOT,
        }))
    return HttpResponse(html)

def show_pages(request, page_unique_name):
    tmp = get_template('page.html')

    content = page.objects.filter(unique_id=page_unique_name)[0]

    html = tmp.render(Context({
            'title': content.page_name + ' | ' +info_dict['site_name'],
            'site_keywords': content.keywords,
            'site_description': content.description,
            'site_logo': info_dict['site_logo'],
            'site_address': info_dict['site_address'],
            'icp': info_dict['icp'],
            'tel': info_dict['tel'],
            'fax': info_dict['fax'],
            'qq': info_dict['qq'],
            'email': info_dict['email'],
            'page_content': content.content
        }))
    return HttpResponse(html)
