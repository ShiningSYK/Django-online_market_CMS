from django.db import models
from commodity.models import CommodityDetail
from enums import PaymentChoices, IsDeletedChoices, IsInCart,IsMale


# Create your models here.
class UserInfo(models.Model):
    id = models.AutoField('序号', primary_key=True)
    username = models.CharField('用户名', max_length=20)
    password = models.CharField('密码', max_length=10)
    gender = models.PositiveIntegerField('性别',choices=[(k, v) for k, v in IsMale.items()],default=0)
    nickname = models.CharField('昵称', max_length=50)
    email = models.CharField('邮箱',max_length=100)
    phone = models.CharField('手机号',max_length=100,default="123456")
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('修改时间', auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user_info'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


class UserOrder(models.Model):
    id = models.AutoField('序号', primary_key=True)
    user = models.ForeignKey(verbose_name='用户', to=UserInfo, to_field='id', on_delete=models.CASCADE)
    price = models.PositiveIntegerField('价格', )
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    payment_type = models.PositiveIntegerField('支付类型', choices=[(k, v) for k, v in PaymentChoices.items()], null=False,
                                               blank=False)

    def payment(self):
        if self.payment_type == 0:
            return "支付宝"
        else:
            return "微信"

    payment.short_description = '支付方式'

    class Meta:
        db_table = 'user_order'
        verbose_name = '用户订单'
        verbose_name_plural = verbose_name


class CartDetail(models.Model):
    id = models.AutoField('序号', primary_key=True)
    user = models.ForeignKey(verbose_name='用户', to=UserInfo, to_field='id', on_delete=models.CASCADE)
    commodity = models.ForeignKey(verbose_name='商品', to=CommodityDetail, to_field='id', on_delete=models.CASCADE)
    commodity_amount = models.PositiveSmallIntegerField('数量', null=False, blank=False)
    status = models.PositiveIntegerField('是否购买', choices=[(k, v) for k, v in IsInCart.items()], default=0, null=False,
                                         blank=False)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('修改时间', auto_now=True, blank=True, null=True)
    is_deleted = models.PositiveIntegerField('是否删除', choices=[(k, v) for k, v in IsDeletedChoices.items()], default=0,
                                             null=False, blank=False)

    def b_status(self):
        # 0表示未失效，1表示失效
        if self.status == 0:
            return False
        else:
            return True

    def b_deleted(self):
        # 0表示未删除，1表示删除
        if self.is_deleted == 0:
            return False
        else:
            return True

    b_status.boolean = True
    b_status.short_description = '是否失效'
    b_deleted.boolean = True
    b_deleted.short_description = '是否删除'

    class Meta:
        db_table = 'cart_detail'
        verbose_name = '购物车'
        verbose_name_plural = verbose_name
