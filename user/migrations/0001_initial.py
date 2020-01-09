# Generated by Django 3.0.1 on 2020-01-01 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('commodity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('username', models.CharField(max_length=20, verbose_name='用户名')),
                ('password', models.CharField(max_length=10, verbose_name='密码')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'db_table': 'user_info',
            },
        ),
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('price', models.PositiveIntegerField(verbose_name='价格')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('payment_type', models.PositiveIntegerField(verbose_name='支付类型')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserInfo', verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户订单',
                'verbose_name_plural': '用户订单',
                'db_table': 'user_order',
            },
        ),
        migrations.CreateModel(
            name='CartDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('commodity_amount', models.PositiveSmallIntegerField(verbose_name='数量')),
                ('status', models.PositiveIntegerField(default=0, verbose_name='是否失效')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('is_deleted', models.PositiveIntegerField(default=0, verbose_name='是否删除')),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commodity.CommodityDetail', verbose_name='商品')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserInfo', verbose_name='用户')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
                'db_table': 'cart_detail',
            },
        ),
    ]
