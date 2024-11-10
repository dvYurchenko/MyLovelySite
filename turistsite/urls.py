from django.contrib import admin
from django.urls import path, URLPattern
from turistsite import views
from turistsite.views import first
from django.views import View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('first/', views.first, name='first'),
    path('second/', views.second, name='second')
]