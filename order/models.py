from django.db import models
from user.models import UserOrder

# Create your models here.

class OrderDetail(models.Model):
    id = models.AutoField('序号',primary_key=True)
    order = models.ForeignKey(verbose_name='订单号',to=UserOrder, to_field='id',on_delete=models.CASCADE)
    commodity_id = models.IntegerField('商品号')
    commodity_name = models.CharField('商品名称',max_length=20)
    commodity_price = models.PositiveIntegerField('商品单价')
    commodity_amount = models.PositiveSmallIntegerField('商品数量')
    commodity_discount = models.DecimalField('商品折扣',max_digits=10, decimal_places=0, blank=True, null=True)
    commodity_image = models.CharField('商品图片',max_length=300)

    class Meta:
        db_table = 'order_detail'
        verbose_name = "订单详情"
        verbose_name_plural = verbose_name
