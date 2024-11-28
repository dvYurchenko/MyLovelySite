# Generated by Django 3.2.25 on 2024-11-08 07:13

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turistsite', '0006_alter_mytour_image_1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mytour',
            name='number',
        ),
        migrations.AlterField(
            model_name='mytour',
            name='description_1',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Описание_1'),
        ),
        migrations.AlterField(
            model_name='mytour',
            name='title',
            field=models.TextField(max_length=120, verbose_name='Название'),
        ),
    ]