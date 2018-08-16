# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class News(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    标题 = models.CharField(max_length=500, blank=True, null=True)
    日期 = models.CharField(max_length=30, blank=True, null=True)
    内容 = models.TextField(blank=True, null=True)
    url = models.CharField(db_column='URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    来源 = models.CharField(max_length=50, blank=True, null=True)
    采集时间 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'
