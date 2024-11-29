from distutils.command.register import register
from django.contrib import admin
from turistsite.models import Booking1, MyTour

admin.site.register(MyTour)
admin.site.register(Booking1)



