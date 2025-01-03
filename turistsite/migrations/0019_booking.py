# Generated by Django 3.2.25 on 2024-11-21 06:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turistsite', '0018_auto_20241114_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=' ', max_length=50)),
                ('last_name', models.CharField(default=' ', max_length=50)),
                ('title_of_trip', models.CharField(default=' ', max_length=50)),
                ('col_of_ank', models.IntegerField(default=0)),
                ('col_of_child', models.IntegerField(default=0)),
                ('price_ank', models.IntegerField(default=0)),
                ('price_child', models.IntegerField(default=0)),
                ('checkin_date', models.DateField(choices=[('date_1', 'date_1'), ('date_2', 'date_2'), ('date_3', 'date_3'), ('date_4', 'date_4')], default=datetime.datetime.now)),
                ('email', models.EmailField(default=' ', max_length=254)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
