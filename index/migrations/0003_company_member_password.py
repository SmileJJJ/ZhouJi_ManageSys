# Generated by Django 2.1.1 on 2018-09-15 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20180910_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_member',
            name='password',
            field=models.CharField(default='123456', max_length=12, verbose_name='登录密码'),
        ),
    ]
