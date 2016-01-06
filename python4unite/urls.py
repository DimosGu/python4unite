from django.conf.urls import patterns, include, url
from django.conf import settings

from heyi.views import index, product_cate, contactus, show_pages, product_display
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'python4unite.views.home', name='home'),
    # url(r'^python4unite/', include('python4unite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', index),
    url(r'^index/$', index),
    url(r'^product_category/$', product_cate),
    url(r'^products_category/(.+)/$', product_cate),
    url(r'^product/(.+)/(.+)/$', product_display),
    url(r'^contactus/$', contactus),
    url(r'^pages/(.+)/$', show_pages)
)

#handler404 = 'heyi.views.page_not_found'
if settings.DEBUG is False:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT, }),
   )
