from distutils.command.register import register
from django.contrib import admin
from turistsite.models import Booking, MyTour

admin.site.register(MyTour)
admin.site.register(Booking)


class ModelAdmin:
    pass