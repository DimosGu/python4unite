#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models import config, show, nav, page, product, product_category

def rewrite_url(module, value=''):
    '''
    if value.isdigit():
        id = value
    else:
        rec = value

    filename = '' if module != 'page' else '/' + id
    url = get_unique(module, id) + filename + '/'
    return url
    '''
    if module == 'nav':
        url = value
    elif module == 'page':
        if int(value) > 0:
            url = '/pages/' + get_unique(module, int(value)) + '/'
        else:
            url = '/pages/'
    else:
        url = '/' + module + '/'
    return url

'''站点信息'''
def get_site_info():
    site_info = config.objects.all()
    info_dict = {}
    for info in site_info:
        info_dict[info.name] = info.value
    return info_dict

'''获取导航菜单'''
def get_nav(type='middle', parent_id=0, current_module='', current_id='', current_parent_id=''):
    nav_list = []
    data = nav.objects.all()
    for value in data:
        nav_item = {}
        if value.parent_id == parent_id and value.type == type:
            nav_item['url'] = rewrite_url(value.module, value.guide)
            nav_item['nav_name'] = value.nav_name
            nav_item['child'] = []
            for child in data:
                if child.parent_id == value.id:
                    child_item = {}
                    child_item['url'] = rewrite_url(child.module, child.guide)
                    child_item['nav_name'] = child.nav_name
                    nav_item['child'].append(child_item)
            nav_list.append(nav_item)
    return nav_list



'''幻灯片列表'''
def get_slide_show():
    site_show = show.objects.all()
    show_slide = []
    for slide in site_show:
        #show_slide.append(slide.show_img)
        show_slide.append({'slide_name':slide.show_name, 'slide_img':slide.show_img})
        #show_slide[slide.show_name] = slide.show_img

    return show_slide

'''获取子分类'''
def get_child_id(data, parent_id=0):
    childs = []
    childs.append(parent_id)
    for item in data:
        if item.parent_id == parent_id:
            childs.append(item.cat_id)
            childs = childs + get_child_id(data, item.cat_id)
    return childs

'''获取分类ID'''
def get_cate_id(module, unique_name):
    item = product_category.objects.get(unique_id=unique_name)
    return int(item.cat_id)

'''获取分类unique_name'''
def get_unique(module, id):
    item = None
    if module == 'product_category':
        item = product_category.objects.get(cat_id=id)
    elif module == 'page':
        item = page.objects.get(id=id)

    return str(item.unique_id) if item is not None else ''
