# Generated by Django 3.2.25 on 2024-11-27 16:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('turistsite', '0021_auto_20241126_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking1',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='booking1',
            name='checkin_date',
            field=models.DateField(choices=[('date_1', 'date_1'), ('date_2', 'date_2'), ('date_3', 'date_3')], default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='booking1',
            name='col_of_ank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_price_ank', to='turistsite.mytour'),
        ),
        migrations.AlterField(
            model_name='booking1',
            name='email',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Price_for_ank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_ank', models.IntegerField(default=0, verbose_name='Цена взрослый')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turistsite.mytour', verbose_name='Название')),
            ],
        ),
    ]
