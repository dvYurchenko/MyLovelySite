# Generated by Django 3.2.25 on 2024-11-08 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turistsite', '0005_mytour_image_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytour',
            name='image_1',
            field=models.ImageField(default='static/images/image1/strelka.jpg', upload_to='image1', verbose_name='Изображения'),
        ),
    ]
