# Generated by Django 3.0.1 on 2020-01-02 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0005_auto_20200102_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodityimage',
            name='commodity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_commodity_pics', to='commodity.CommodityDetail', verbose_name='商品名称'),
        ),
    ]
