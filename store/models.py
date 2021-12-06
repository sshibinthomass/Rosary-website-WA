from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.db.models import F

TAG_CHOICES = (
    ('None','None'),
    ('On Offer', 'On Offer'),
    ('Fast Selling','Fast Selling'),
    ('New','New'),
)


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)

class Risk(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'risks'

    def get_absolute_url(self):
        return reverse('store:risk_list', args=[self.slug])

    def __str__(self):
        return self.name

class Watering(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'waterings'

    def get_absolute_url(self):
        return reverse('store:watering_list', args=[self.slug])

    def __str__(self):
        return self.name

class maintenance(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'maintenances'

    def get_absolute_url(self):
        return reverse('store:maintenance_list', args=[self.slug])

    def __str__(self):
        return self.name

class Sun(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'suns'

    def get_absolute_url(self):
        return reverse('store:sun_list', args=[self.slug])

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name

class Product(models.Model):
    pid=models.IntegerField(null=False)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE,default=7)
    risk = models.ForeignKey(Risk, related_name='product', on_delete=models.CASCADE,default=1)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator',default=1)
    title = models.CharField(max_length=255)
    Nickname=models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    slug = models.SlugField(max_length=255)
    size=models.CharField(max_length=255, default="2-3")
    price = models.IntegerField(default=0)
    disprice = models.IntegerField(default=0)
    orgprice = models.IntegerField(default=0)
    in_stock = models.BooleanField(default=True)
    indoor = models.BooleanField(default=False)
    mother = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    sun = models.ForeignKey(Sun, related_name='product', on_delete=models.CASCADE,default=1)
    Watering = models.ForeignKey(Watering, related_name='product', on_delete=models.CASCADE,default=1)
    products = ProductManager()
    maintenance = models.ForeignKey(maintenance, related_name='product', on_delete=models.CASCADE,default=1)
    tag = models.CharField(max_length=20, choices=TAG_CHOICES, default='None')


    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.title

