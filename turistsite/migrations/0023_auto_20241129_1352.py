# Generated by Django 3.2.25 on 2024-11-29 08:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('turistsite', '0022_auto_20241127_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking1',
            name='price',
        ),
        migrations.RemoveField(
            model_name='booking1',
            name='price_ank',
        ),
        migrations.RemoveField(
            model_name='booking1',
            name='price_child',
        ),
        migrations.AlterField(
            model_name='booking1',
            name='checkin_date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Дата поездки'),
        ),
        migrations.AlterField(
            model_name='booking1',
            name='col_of_ank',
            field=models.IntegerField(default=0, verbose_name='Количество взрослых'),
        ),
        migrations.AlterField(
            model_name='booking1',
            name='col_of_child',
            field=models.IntegerField(default=0, verbose_name='Количество детей'),
        ),
        migrations.AlterField(
            model_name='booking1',
            name='email',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Email'),
        ),
        migrations.DeleteModel(
            name='Price_for_ank',
        ),
    ]