# Generated by Django 3.0.1 on 2020-01-02 06:18

import commodity.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0003_auto_20200102_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodityimage',
            name='image_url',
            field=models.ImageField(upload_to=commodity.models.CommodityImage.img_path, verbose_name='图片'),
        ),
    ]
