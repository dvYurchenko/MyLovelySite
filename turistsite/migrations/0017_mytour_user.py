# Generated by Django 3.2.25 on 2024-11-14 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turistsite', '0016_alter_customuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytour',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
