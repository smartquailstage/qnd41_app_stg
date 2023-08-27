from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

class Category(models.Model):
    CATEGORY_TYPES=[
        ('danger','danger'),
        ('warning','warning'),
        ('info','info'),
        ('secondary','secondary'),
        ('default','default'),
    ]
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)
    type = models.CharField(null=True, choices=CATEGORY_TYPES,max_length=20)
    logo = models.ImageField(upload_to='logos/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    video = models.URLField(null=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('services:product_list_by_category',
                           args=[self.slug])

class CrewCategoryItem(models.Model):
    user = models.ForeignKey(User,
                              related_name='users',
                              on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='smartbusinesscrew/%Y/%m/%d',
                              blank=True)
    category = models.ForeignKey(Category,
                                related_name='service',
                                on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200,db_index=True)
    apellido = models.CharField(max_length=200,db_index=True)
    edad = models.PositiveIntegerField(default=1)
    años_experiencia = models.PositiveIntegerField(default=1)
    about_me = models.TextField(blank=True)
    email = models.EmailField()
    insta = models.URLField(null=True)
    face = models.URLField(null=True)
    tiktok = models.URLField(null=True)

    def __str__(self):
        return '{}'.format(self.id)


class Product(models.Model):
    SERVICES_TYPES=[
        ('Frontend','Frontend'),
        ('Backend','Backend'),
    ]
    TYPES=[
        ('primary','primary'),
        ('warning','warning'),
        ('success','success'),
        ('danger','danger'),
    ]
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    serices_types = models.CharField(null=True, choices=SERVICES_TYPES,max_length=20)
    types = models.CharField(null=True, choices=TYPES,max_length=20)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('services:product_detail',
                           args=[self.id, self.slug])


class Service_Product(models.Model):
    SERVICES_TYPES=[
        ('Frontend','Frontend'),
        ('Backend','Backend'),
    ]
    TYPES=[
        ('primary','primary'),
        ('warning','warning'),
        ('success','success'),
        ('danger','danger'),
    ]
    product = models.ForeignKey(Product,
                                 related_name='services',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    serices_types = models.CharField(null=True, choices=SERVICES_TYPES,max_length=20)
    types = models.CharField(null=True, choices=TYPES,max_length=20)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('product_services:produc_servicest_detail',
                           args=[self.id, self.slug])