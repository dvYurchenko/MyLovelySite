# Generated by Django 3.2.25 on 2024-11-10 06:30

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turistsite', '0011_mytour_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytour',
            name='title',
            field=ckeditor.fields.RichTextField(max_length=120, verbose_name='Название'),
        ),
    ]