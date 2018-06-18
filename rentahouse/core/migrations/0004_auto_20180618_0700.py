# Generated by Django 2.0.6 on 2018-06-18 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180618_0654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imovel',
            name='vl_condominio',
        ),
        migrations.AlterField(
            model_name='imovel',
            name='tipo',
            field=models.CharField(choices=[('Apartamento', 'Apartamento'), ('Casa', 'Casa'), ('Condomínio fechado', 'Condomínio fechado'), ('Sobrado', 'Sobrado')], max_length=20),
        ),
    ]