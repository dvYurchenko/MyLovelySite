# Generated by Django 3.2.25 on 2024-11-08 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turistsite', '0009_alter_mytour_image_1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mytour',
            name='image_1',
        ),
    ]