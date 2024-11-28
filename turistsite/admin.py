from distutils.command.register import register
from django.contrib import admin
from turistsite.models import Booking1, MyTour, Price_for_ank

admin.site.register(MyTour)
admin.site.register(Booking1)
admin.site.register(Price_for_ank)


