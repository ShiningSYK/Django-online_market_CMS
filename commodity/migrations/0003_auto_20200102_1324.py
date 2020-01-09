# Generated by Django 3.0.1 on 2020-01-02 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0002_auto_20200102_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commoditydetail',
            name='commodity_info',
            field=models.TextField(max_length=255, verbose_name='商品描述'),
        ),
        migrations.AlterField(
            model_name='commoditydetail',
            name='is_discount',
            field=models.PositiveIntegerField(choices=[(0, '不打折'), (1, '打折')], default=0, verbose_name='是否打折'),
        ),
        migrations.AlterField(
            model_name='commodityimage',
            name='image_url',
            field=models.CharField(max_length=100, verbose_name='图片'),
        ),
    ]