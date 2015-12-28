from django.db import models

# Create your models here.

class admin(models.Model):
    """docstring for Admin"""
    user_id     = models.SmallIntegerField(primary_key=True)
    user_name   = models.CharField(max_length=60)
    email       = models.EmailField(max_length=60)
    password    = models.CharField(max_length=32)
    action_list = models.TextField()
    add_time    = models.IntegerField()
    last_login  = models.IntegerField()
    last_ip     = models.CharField(max_length=15)

class admin_log(models.Model):
    """docstring for admin_log"""
    create_time = models.IntegerField()
    user_id     = models.SmallIntegerField()
    action      = models.CharField(max_length=255)
    ip          = models.CharField(max_length=15)

class article(models.Model):
    """docstring for article"""
    cat_id          = models.SmallIntegerField()
    title           = models.CharField(max_length=150)
    defined         = models.TextField()
    content         = models.TextField()
    image           = models.CharField(max_length=255)
    keywords        = models.CharField(max_length=255)
    add_time        = models.IntegerField()
    description     = models.CharField(max_length=255)
    home_sort       = models.CharField(max_length=2)
    class Meta:
        ordering = ['home_sort']

class article_category(models.Model):
    """docstring for article_category"""
    cat_id      = models.SmallIntegerField(primary_key=True)
    unique_id   = models.CharField(max_length=30)
    cat_name    = models.CharField(max_length=255)
    keywords    = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    parent_id   = models.SmallIntegerField()
    sort        = models.SmallIntegerField()
    class Meta:
        ordering = ['sort']


class config(models.Model):
    """docstring for config"""
    name    = models.CharField(max_length=80)
    value   = models.TextField()
    type    = models.CharField(max_length=10)
    box     = models.CharField(max_length=255)
    tab     = models.CharField(max_length=10)
    sort    = models.SmallIntegerField()
    class Meta:
        ordering = ['sort']

class guestbook(models.Model):
    """docstring for guestbook"""
    title       = models.CharField(max_length=150)
    name        = models.CharField(max_length=60)
    contact_type = models.CharField(max_length=30)
    contact     = models.CharField(max_length=150)
    content     = models.TextField()
    if_show     = models.SmallIntegerField()
    if_read     = models.SmallIntegerField()
    ip          = models.CharField(max_length=15)
    add_time    = models.IntegerField()
    reply_id    = models.SmallIntegerField()

class link(models.Model):
    """docstring for link"""
    link_name   = models.CharField(max_length=60)
    link_url    = models.CharField(max_length=255)
    sort        = models.SmallIntegerField()
    class Meta:
        ordering = ['sort']

class nav(models.Model):
    """docstring for nav"""
    module      = models.CharField(max_length=20)
    nav_name    = models.CharField(max_length=50)
    guide       = models.CharField(max_length=50)
    parent_id   = models.SmallIntegerField()
    type        = models.CharField(max_length=10)
    sort        = models.SmallIntegerField()
    class Meta:
        ordering = ['sort']

class page(models.Model):
    """docstring for page"""
    unique_id   = models.CharField(max_length=30)
    parent_id   = models.SmallIntegerField()
    page_name   = models.CharField(max_length=150)
    content     = models.TextField()
    keywords    = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class product(models.Model):
    """docstring for product"""
    cat_id          = models.SmallIntegerField()
    product_name    = models.CharField(max_length=150)
    price           = models.DecimalField(max_digits=10, decimal_places=2)
    defined         = models.TextField()
    content         = models.TextField()
    product_image   = models.CharField(max_length=255)
    keywords        = models.CharField(max_length=255)
    add_time        = models.IntegerField()
    description     = models.CharField(max_length=255)
    home_sort       = models.CharField(max_length=2)
    class Meta:
        ordering = ['home_sort']

class product_category(models.Model):
    """docstring for product_category"""
    cat_id      = models.SmallIntegerField(primary_key=True)
    unique_id   = models.CharField(max_length=30)
    cat_name    = models.CharField(max_length=255)
    keywords    = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    parent_id   = models.SmallIntegerField()
    sort        = models.SmallIntegerField()
    class Meta:
        ordering = ['sort']

class show(models.Model):
    """docstring for show"""
    show_name   = models.CharField(max_length=60)
    show_link   = models.CharField(max_length=255)
    show_img    = models.CharField(max_length=255)
    type        = models.CharField(max_length=10)
    sort        = models.SmallIntegerField()
    class Meta:
        ordering = ['sort']
