# -*- coding:utf-8 -*-
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.db import connection
from python4unite.settings import SITE_ROOT
from models import config, show, page, product, product_category, nav
from common import get_child_id, get_cate_id, get_unique, get_category, get_nav, get_page_list, ur_here, pager
from init import *
import time

def index(request):
    tmp = get_template('index.html')

    nav_list = get_nav('middle', 0, '')

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
def product_list_all(request, page='1'):
    tmp = get_template('product_cate.html')
    page = int(page)

    product_cate_set = product_category.objects.all()
    cate_id = 0
    childs = get_child_id(product_cate_set, cate_id)
    product_cate = get_category('product_category', 0, cate_id)

    urhere = ur_here('product_category', cate_id)
    page_list = pager('product_category', 10, page, childs)

    cur = connection.cursor()
    child_str = ''
    for childid in childs:
        child_str += str(childid) + ','
    #product_set = product.objects.filter(cat_id__in = childs)
    r = cur.callproc('proc_product_list', [child_str,page,10])
    product_set = cur.fetchall()
    cur.close()
    product_list = []
    for single_product in product_set:
        item = {}
        item['id']              = single_product[0]
        item['cat_id']          = single_product[1]
        item['product_name']    = single_product[2]
        item['content']         = single_product[4]
        item['product_image']   = single_product[3]
        dt = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(single_product[7])))
        item['add_time']        = dt
        item['description']     = single_product[6]
        item['url']             = '/product/' + get_unique('product_category', item['cat_id']) + '/' + str(item['id']) + '/'
        product_list.append(item)

    nav_list = get_nav('middle', 0, 'product_category')

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
            'product_cate': product_cate,
            'ur_here': urhere,
            'page_list':page_list,
        }))
    return HttpResponse(html)

def product_list_cate(request, unique_name='all', page='1'):
    tmp = get_template('product_cate.html')
    page = int(page)

    product_cate_set = product_category.objects.all()
    cate_id = get_cate_id('product_category', unique_name)
    childs = get_child_id(product_cate_set, cate_id)
    product_cate = get_category('product_category', 0, cate_id)

    page_list = pager('product_category', 10, page, childs, unique_name)

    urhere = ur_here('product_category', cate_id)

    cur = connection.cursor()
    child_str = ''
    for childid in childs:
        child_str += str(childid) + ','
    #product_set = product.objects.filter(cat_id__in = childs)
    r = cur.callproc('proc_product_list', [child_str,page,10])
    product_set = cur.fetchall()
    cur.close()
    product_list = []
    for single_product in product_set:
        item = {}
        item['id']              = single_product[0]
        item['cat_id']          = single_product[1]
        item['product_name']    = single_product[2]
        item['content']         = single_product[4]
        item['product_image']   = single_product[3]
        dt = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(single_product[7])))
        item['add_time']        = dt
        item['description']     = single_product[6]
        item['url']             = '/product/' + get_unique('product_category', item['cat_id']) + '/' + str(item['id']) + '/'
        product_list.append(item)

    nav_list = get_nav('middle', 0, 'product_category')

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
            'product_cate': product_cate,
            'ur_here': urhere,
            'page_list':page_list,
        }))
    return HttpResponse(html)

# 显示产品详情
def product_display(request, cate_unique_name, product_id):
    tmp = get_template('product.html')
    nav_list = get_nav('middle', 0, '')

    product_cate = get_category('product_category', 0, 0)

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

    urhere = ur_here('product_category', int(item['cat_id']), item['product_name'])

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
            'product_cate': product_cate,
            'ur_here': urhere,
        }))
    return HttpResponse(html)

def contactus(request):
    tmp = get_template('contactus.html')
    nav_list = get_nav('middle', 0, 'contactus')

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
    # 页面ID
    page_id = get_cate_id('page', page_unique_name)
    nav_list = get_nav('middle', 0, 'page', page_id)

    page_list = get_page_list(0, page_id)

    content = page.objects.filter(unique_id=page_unique_name)[0]

    urhere = ur_here('page', int(page_id))

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
            'page_list': page_list,
            'ur_here': urhere,
        }))
    return HttpResponse(html)

def page_not_found(request):
    return render_to_response('404.html')
