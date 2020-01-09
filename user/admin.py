from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    # 编辑页看到的字段
    fields = ['username','password','nickname','email','gender','phone']
    # 首页看到的字段
    list_display = ['id','nickname','email','username','password','gender','phone','create_time']
    # 搜索框支持的搜索字段
    search_fields = ['username']

@admin.register(UserOrder)
class UserOrderAdmin(admin.ModelAdmin):
    # 编辑页看到的字段
    fields = ['user', 'price','payment_type']
    # 首页看到的字段
    list_display = ['id', 'user', 'price','payment','create_time']
    # 搜索框支持的搜索字段
    search_fields = ['user','payment_type']

@admin.register(CartDetail)
class CartDetailAdmin(admin.ModelAdmin):
    # 编辑页看到的字段
    fields = ['user', 'commodity','commodity_amount','status',]
    # 首页看到的字段
    list_display = ['id', 'user', 'commodity','commodity_amount','b_status','b_deleted']
    # 搜索框支持的搜索字段
    search_fields = ['user']