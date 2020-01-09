from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(CommodityType)
class CommodityTypeAdmin(admin.ModelAdmin):
    fields = ['type_name','parent','is_deleted']
    list_display = ['id','type_name','parent','b_deleted']
    search_fields = ['type_name']
    empty_value_display = '无'
    ordering = ['id']

class PicsInline(admin.TabularInline):
    model = CommodityImage
    extra = 4
    fields = ['image_url']

@admin.register(CommodityDetail)
class CommodityDetailAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields' : ['commodity_type','commodity_name','commodity_info','commodity_price',
              'commodity_status','is_discount']}),
    ]
    inlines = [PicsInline]
    list_display = ['id','commodity_type','commodity_name','commodity_info','commodity_price',
              'commodity_status','b_discount','b_deleted']
    ordering = ['id']

@admin.register(CommodityImage)
class CommodityImageAdmin(admin.ModelAdmin):
    fields = ['commodity','image_url',]
    list_display = ['id', 'commodity','img',]
    ordering = ['id']