from django.db import models
from commodity.models import CommodityDetail
from enums import IsStartedChoices


# Create your models here.
class ActivityType(models.Model):
    id = models.AutoField('序号', primary_key=True)
    type_name = models.CharField('类型名称', max_length=10)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('修改时间', auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.type_name

    class Meta:
        db_table = 'activity_type'
        verbose_name = "活动类型"
        verbose_name_plural = verbose_name


class ActivityDetail(models.Model):
    id = models.AutoField('序号', primary_key=True)
    activity_name = models.CharField('活动名称', max_length=15)
    activity_type = models.ForeignKey(verbose_name='活动类型', to=ActivityType, to_field='id',on_delete=models.CASCADE)
    activity_info = models.TextField('活动详情', max_length=50, blank=True, null=True)
    activity_status = models.PositiveIntegerField('活动状态', choices=[(k, v) for k, v in IsStartedChoices.items()],
                                                  default=0)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('修改时间', auto_now=True, blank=True, null=True)

    def b_started(self):
        # 0表示未删除，1表示删除
        if self.activity_status == 2:
            return True
        else:
            return False

    b_started.boolean = True
    b_started.short_description = '是否开始'

    def __str__(self):
        return self.activity_name

    class Meta:
        db_table = 'activity_detail'
        verbose_name = '活动详情'
        verbose_name_plural = verbose_name


class RelActivityCommodity(models.Model):
    id = models.AutoField('序号', primary_key=True)
    activity = models.ForeignKey(verbose_name='活动名称', to=ActivityDetail, to_field='id', on_delete=models.CASCADE)
    commodity = models.ForeignKey(verbose_name='商品名称', to=CommodityDetail, to_field='id',on_delete=models.CASCADE)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('修改时间', auto_now=True, blank=True, null=True)

    class Meta:
        db_table = 'rel_activity_commodity'
        verbose_name = '活动商品'
        verbose_name_plural = verbose_name
