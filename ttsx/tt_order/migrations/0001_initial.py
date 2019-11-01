# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tt_goods', '0001_initial'),
        ('tt_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetailInfo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('count', models.IntegerField()),
                ('goods', models.ForeignKey(to='tt_goods.GoodsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('oid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('odate', models.DateTimeField(auto_now_add=True)),
                ('oStatus', models.IntegerField(default=0)),
                ('ototal', models.DecimalField(decimal_places=2, max_digits=6)),
                ('oaddress', models.CharField(max_length=150)),
                ('user', models.ForeignKey(to='tt_user.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='orderdetailinfo',
            name='order',
            field=models.ForeignKey(to='tt_order.OrderInfo'),
        ),
    ]
