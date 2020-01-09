from django.contrib import admin
from .models import OrderDetail
# Register your models here.
@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    fields = ['order','commodity_id','commodity_name','commodity_price','commodity_amount','commodity_discount']
    list_display = ['id','commodity_id','commodity_name','commodity_price','commodity_amount','commodity_discount']