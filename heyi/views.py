# -*- coding:utf-8 -*-
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from python4unite.settings import SITE_ROOT
from models import config, show, page, product, product_category
from common import get_child_id, get_cate_id, get_unique
from init import *
import time

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
            'nav': nav_list,
        }))
    return HttpResponse(html)

# 产品列表
def product_cate(request, unique_name='all'):
    tmp = get_template('product_cate.html')

    product_cate_set = product_category.objects.all()
    if unique_name == 'all':
        cate_id = 0
    else:
        cate_id = get_cate_id('product_category', unique_name)
    childs = get_child_id(product_cate_set, cate_id)

    product_set = product.objects.filter(cat_id__in = childs)
    product_list = []
    for single_product in product_set:
        item = {}
        item['id']              = single_product.id
        item['cat_id']          = single_product.cat_id
        item['product_name']    = single_product.product_name
        item['price']           = 0.00
        item['content']         = single_product.content
        item['product_image']   = single_product.product_image
        dt = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(single_product.add_time)))
        item['add_time']        = dt
        item['description']     = single_product.description
        item['url']             = '/product/' + get_unique('product_category', item['cat_id']) + '/' + str(single_product.id) + '/'
        product_list.append(item)

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
            'nav': nav_list,
        }))
    return HttpResponse(html)

# 显示产品详情
def product_display(request, cate_unique_name, product_id):
    tmp = get_template('product.html')

    single_product= product.objects.get(id = product_id)
    item = {}
    item['id']              = single_product.id
    item['cat_id']          = single_product.cat_id
    item['product_name']    = single_product.product_name
    item['price']           = 0.00
    item['content']         = single_product.content
    item['product_image']   = single_product.product_image
    dt = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(single_product.add_time)))
    item['add_time']        = dt
    item['keywords']        = single_product.keywords
    item['description']     = single_product.description
    item['url']             = get_unique('product_category', item['cat_id']) + '/' + str(single_product.id) + '/'

    html = tmp.render(Context({
            'title': item['product_name'] + ' | ' + info_dict['site_name'],
            'site_logo': info_dict['site_logo'],
            'site_address': info_dict['site_address'],
            'icp': info_dict['icp'],
            'tel': info_dict['tel'],
            'fax': info_dict['fax'],
            'qq': info_dict['qq'],
            'email': info_dict['email'],
            'item':item,
            'nav': nav_list,
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
            'nav': nav_list,
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
            'page_content': content.content,
            'nav': nav_list,
        }))
    return HttpResponse(html)

def page_not_found(request):
    return render_to_response('404.html')
