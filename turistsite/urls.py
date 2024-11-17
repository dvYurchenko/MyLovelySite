from django.contrib import admin
from django.urls import path, URLPattern
from turistsite import views
from turistsite.views import first
from django.views import View
from .views import signup_view, login_view

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('first/', views.first, name='first'),
    path('second/', views.second, name='second'),
    path('third/', views.third, name='third'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
]