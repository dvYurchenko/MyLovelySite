# Generated by Django 3.2.25 on 2024-11-07 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turistsite', '0003_alter_mytour_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytour',
            name='number',
            field=models.IntegerField(default=1, verbose_name='Номер записи'),
        ),
    ]
