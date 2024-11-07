from distutils.command.register import register
from django.contrib import admin
from turistsite.models import MyTour

admin.site.register(MyTour)
