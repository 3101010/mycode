# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-31 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20171231_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service_Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': '业务分组表',
                'db_table': 'opsmanage_service_assets',
                'verbose_name': '业务分组表',
                'permissions': (('can_read_service_assets', '读取业务资产权限'), ('can_change_service_assets', '更改业务资产权限'), ('can_add_service_assets', '添加业务资产权限'), ('can_delete_service_assets', '删除业务资产权限')),
            },
        ),
    ]