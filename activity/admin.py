from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(ActivityType)
class ActivityTypeAdmin(admin.ModelAdmin):
    fields = ['type_name']
    list_display = ['id', 'type_name']


@admin.register(ActivityDetail)
class ActivityDetailAdmin(admin.ModelAdmin):
    fields = ['activity_name', 'activity_type', 'activity_info', 'activity_status']
    list_display = ['id', 'activity_name', 'activity_type', 'activity_info', 'b_started']

@admin.register(RelActivityCommodity)
class RelActivityCommodity(admin.ModelAdmin):
    fields = ['activity','commodity']
    list_display = ['activity','commodity']
    ordering = ['activity']