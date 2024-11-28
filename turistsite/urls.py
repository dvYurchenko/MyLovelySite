from django.contrib import admin
from django.urls import path, URLPattern
from turistsite import views
from turistsite.views import contacts, about
from django.views import View
from .views import signup_view, login_view , booking

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('first/', views.first, name='first'),
    path('second/', views.second, name='second'),
    path('third/', views.third, name='third'),
    path('signup/', signup_view, name='signup'),
    path('about/', about, name='about'),
    path('login/', login_view, name='login'),
    path('contacts', contacts, name='contacts'),
    path('booking/', booking, name='booking'),
    path('logout/', views.sign_out, name='logout')
]