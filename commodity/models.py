from django.db import models
from enums import CommodityStatusChoices, IsDiscountChoices, IsDeletedChoices
import os
from django.utils.safestring import mark_safe
from django.db.models.signals import *
from django.dispatch.dispatcher import receiver


# Create your models here.
class CommodityType(models.Model):
    id = models.AutoField('序号', primary_key=True)
    type_name = models.CharField('商品类型', unique=True, max_length=10)
    parent = models.ForeignKey(to='self',to_field='id', on_delete=models.CASCADE, null=True, blank=True, verbose_name='上一级分类',related_name='pid')
    create_date = models.DateTimeField('创建时间', auto_now_add=True)
    update_date = models.DateTimeField('修改时间', auto_now=True, blank=True, null=True)
    is_deleted = models.PositiveIntegerField('是否删除', choices=[(k, v) for k, v in IsDeletedChoices.items()], default=0,
                                             null=False, blank=False)

    def b_deleted(self):
        # 0表示未删除，1表示删除
        if self.is_deleted == 0:
            return False
        else:
            return True

    b_deleted.boolean = True
    b_deleted.short_description = '是否删除'

    def __str__(self):
        return self.type_name

    class Meta:
        db_table = 'commodity_type'
        verbose_name = '商品类型'
        verbose_name_plural = verbose_name


class CommodityDetail(models.Model):
    id = models.AutoField('序号', primary_key=True)
    commodity_type = models.ForeignKey(verbose_name='商品类型', to=CommodityType, to_field='id', on_delete=models.CASCADE,
                                       null=True)
    commodity_name = models.CharField('商品名称', max_length=255)
    commodity_info = models.TextField('商品描述', max_length=255)
    commodity_price = models.PositiveIntegerField('商品单价')
    commodity_status = models.PositiveIntegerField('商品状态', choices=[(k, v) for k, v in CommodityStatusChoices.items()],
                                                   default=0)
    commodity_pics = models.CharField('商品图片', max_length=255, blank=True, null=True)
    is_discount = models.PositiveIntegerField('是否打折', choices=[(k, v) for k, v in IsDiscountChoices.items()], default=0)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('修改时间', auto_now=True, blank=True, null=True)
    is_deleted = models.PositiveIntegerField('是否删除', default=0, null=False, blank=False)

    def b_discount(self):
        # 0表示未不打折，1表示打折
        if self.is_discount == 0:
            return False
        else:
            return True

    b_discount.boolean = True
    b_discount.short_description = '是否打折'

    def b_deleted(self):
        # 0表示未删除，1表示删除
        if self.is_deleted == 0:
            return False
        else:
            return True

    b_deleted.boolean = True
    b_deleted.short_description = '是否删除'

    def __str__(self):
        return self.commodity_name

    class Meta:
        db_table = 'commodity_detail'
        verbose_name = "商品信息"
        verbose_name_plural = "商品信息"


# @receiver(post_save, sender=CommodityDetail)
# def update_pics(sender, **kwargs):
#     commodity = CommodityDetail.objects.last()
#     imgs = commodity.fk_commodity_pics.all()
#     for img in imgs:
#         print("fk img:" + img.__str__())
#     print(commodity)


class CommodityImage(models.Model):

    def img_path(self, filename):
        return os.path.join("imgs", filename)

    id = models.AutoField('序号', primary_key=True)
    commodity = models.ForeignKey(verbose_name='商品名称', related_name='fk_commodity_pics', to=CommodityDetail,
                                  to_field='id', on_delete=models.CASCADE)
    image_url = models.ImageField(verbose_name='图片', upload_to=img_path, blank=True, null=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('修改时间', auto_now=True, blank=True, null=True)
    is_deleted = models.PositiveIntegerField('是否删除', default=0, null=False, blank=False)

    def b_deleted(self):
        # 0表示未删除，1表示删除
        if self.is_deleted == 0:
            return False
        else:
            return True

    b_deleted.boolean = True
    b_deleted.short_description = '是否删除'

    def img(self):
        try:
            img = mark_safe('<img src="%s" width="80px" />' % (self.image_url.url,))
        except Exception as e:
            img = ''
        return img

    img.short_description = u'缩略图'

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'commodity_image'
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name


@receiver(post_save, sender=CommodityImage)
def add_pic2commodity(sender, **kwargs):
   img = CommodityImage.objects.last()
   id = img.id
   print("id:"+str(id))
   commodity = img.commodity
   if commodity.commodity_pics ==None:
       commodity.commodity_pics=f"{id}"
       commodity.save()
   else:
       commodity.commodity_pics+=f",{id}"
       commodity.save()
   print(commodity.commodity_pics)