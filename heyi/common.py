#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models import config, show, nav, page, product, product_category

def rewrite_url(module, value=0):
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
    elif module == 'product_category':
        if int(value) > 0:
            url = '/product_category/' + get_unique(module, int(value)) + '/'
        else:
            url = '/product_category/'
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

'''高亮当前菜单'''
def wcr_current(module, id, current_module, current_id=0, current_parent_id=0):
    if id == current_id and module == current_module:
        return True
    elif (not id) and module == current_module:
        return True
    else:
        return False

'''获取导航菜单'''
def get_nav(type='middle', parent_id=0, current_module='', current_id=0, current_parent_id=0):
    nav_list = []
    home = {'url':'/', 'nav_name':'主页'}
    if current_module == '':
        home['cur'] = False
    else:
        home['cur'] = False
    nav_list.append(home)

    data = nav.objects.all()
    for value in data:
        nav_item = {}
        if value.parent_id == parent_id and value.type == type:
            nav_item['url'] = rewrite_url(value.module, value.guide)
            nav_item['nav_name'] = value.nav_name
            nav_item['cur'] = wcr_current(value.module, int(value.guide), current_module, current_id, current_parent_id)
            nav_item['child'] = []
            for child in data:
                if child.parent_id == value.id:
                    child_item = {}
                    child_item['url'] = rewrite_url(child.module, child.guide)
                    child_item['nav_name'] = child.nav_name
                    child_item['cur'] = wcr_current(child.module, int(child.guide), current_module, current_id, current_parent_id)
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
    if module == 'product_category':
        item = product_category.objects.get(unique_id=unique_name)
        id = int(item.cat_id)
    elif module == 'page':
        item = page.objects.get(unique_id=unique_name)
        id = int(item.id)
    return id

'''获取分类unique_name'''
def get_unique(module, id):
    item = None
    if module == 'product_category':
        item = product_category.objects.get(cat_id=id)
    elif module == 'page':
        item = page.objects.get(id=id)

    return str(item.unique_id) if item is not None else ''

'''当前位置'''
def ur_here(module, cat_id=0, title=''):
    if module == 'onepage':
        title = '<li class="active">' + title + '</li>'
        return title
    main = '<li><a href="' + rewrite_url(module) + '>' + module + '</a></li>'

'''获取分类'''
def get_category(model_name, parent_id=0, current_id=0):
    cate_array = []
    if model_name == 'product_category':
        table_name = product_category
    else:
        return None

    data = table_name.objects.all()
    for value in data:
        item = {}
        if value.parent_id == parent_id:
            item['cat_name'] = value.cat_name
            item['url'] = rewrite_url(model_name, value.cat_id)
            item['cur'] = True if value.cat_id == current_id else False
            item['child'] = []
            for child in data:
                if child.parent_id == value.cat_id:
                    item['child'].append(get_category(model_name, value.cat_id, current_id))
            cate_array.append(item)
    return cate_array

'''获取分类单页列表'''
def get_page_list(parent_id=0, current_id=0):
    page_list = []
    data = page.objects.all()
    for value in data:
        item = {}
        if value.parent_id == parent_id:
            item['page_name'] = value.page_name
            item['url'] = rewrite_url('page', value.id)
            item['cur'] = True if value.id == current_id else False
            page_list.append(item)
    return page_list
