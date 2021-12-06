from django.contrib import admin
from .models import Category, Product,Risk,Sun,Watering,maintenance

@admin.register(Risk)
class RiskAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(maintenance)
class RiskAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Sun)
class SunAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Watering)
class WateringAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pid','title','Nickname','price','is_active','image','maintenance','tag']
    list_filter = [ 'is_active','maintenance','tag','price']
    list_editable = ['is_active','maintenance','image','tag','price']
    prepopulated_fields = {'slug': ('title',)}
    list_per_page= 20
    ordering=['pid']
