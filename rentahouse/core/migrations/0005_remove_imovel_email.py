# Generated by Django 2.0.6 on 2018-06-18 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180618_0700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imovel',
            name='email',
        ),
    ]