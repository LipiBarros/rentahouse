# Generated by Django 2.0.6 on 2018-06-18 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180618_0647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imovel',
            name='qt_vagas_garagem',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
