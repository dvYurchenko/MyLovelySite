# Generated by Django 3.2.25 on 2024-11-08 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turistsite', '0008_auto_20241108_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytour',
            name='image_1',
            field=models.ImageField(blank=True, default='', null=True, upload_to='image1', verbose_name='Изображения'),
        ),
    ]
