#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models import config, show, nav

'''站点信息'''
def get_site_info():
    site_info = config.objects.all()
    info_dict = {}
    for info in site_info:
        info_dict[info.name] = info.value
    return info_dict

'''幻灯片列表'''
def get_slide_show():
    site_show = show.objects.all()
    show_slide = []
    for slide in site_show:
        #show_slide.append(slide.show_img)
        show_slide.append({'slide_name':slide.show_name, 'slide_img':slide.show_img})
        #show_slide[slide.show_name] = slide.show_img

    return show_slide

'''获取导航菜单'''
def get_nav(nav_type='middle', parent_id=0, current_module='', current_id='', current_parent_id=''):
    nav = []
    data = nav.objects.filter(type=nav_type).order_by('sort')
    for item in data:
        item_dict = {}
        if item.parent_id == parent_id and item.type == nav_type:
            if item.module == 'nav':
                pass

    return nav

# 获取站点信息
info_dict = get_site_info()
# 获取幻灯片列表
show_slide = get_slide_show()
