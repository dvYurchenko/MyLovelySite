from cProfile import label

from ckeditor.fields import RichTextField
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser, User




class MyTour(models.Model):
    number = models.IntegerField(verbose_name='Номер тура', default=1)
    title = models.TextField(max_length=120, verbose_name='Название')
    description_1 = models.TextField(verbose_name='Описание_1')
    description_2 = RichTextField(verbose_name='Описание_2')
    image = models.ImageField(upload_to='image1', verbose_name='Изображения', default='')
    date_1 = models.DateField(verbose_name='Дата тура_1', default=datetime.now)
    date_2 = models.DateField(verbose_name='Дата тура_2', default=datetime.now)
    date_3 = models.DateField(verbose_name='Дата тура_3', default=datetime.now)
    date_4 = models.DateField(verbose_name='Дата тура_4', default=datetime.now)
    price_ank = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name='Цена взрослый')
    price_child = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name='Цена ребенок')
    program = RichTextField(verbose_name='Программа тура', default=None)
    includeprice = models.TextField(verbose_name='В стоимость включено', default=None)
    not_includeprice=RichTextField(verbose_name='В стоимость не включено', default=None)
    pamiatka = RichTextField(verbose_name='Памятка туристу', default=None)

    TYPE = [
        ('PERM', 'Туры по Пермскому краю'),
        ('URAL', 'Туры по Уралу'),
        ('ACT', 'Активный отдых'),
        ('CHILD', 'Экскурсии для детей'),
    ]
    type = models.CharField(choices=TYPE, max_length=5, default='PERM', verbose_name='Тип')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Туры'
        verbose_name_plural = 'Туры'

class Booking1(models.Model):
    first_name = models.CharField(max_length=50, default=" ", verbose_name='Имя')
    last_name = models.CharField(max_length=50, default=" ", verbose_name='Фамилия')
    title_of_trip = models.ForeignKey(MyTour, on_delete=models.CASCADE, verbose_name='Название тура')
    col_of_ank = models.IntegerField(default=0, verbose_name='Количество взрослых')
    col_of_child = models.IntegerField(default=0, verbose_name='Количество детей')
    checkin_date = models.DateField(default=datetime.now, verbose_name='Дата поездки')
    email = models.EmailField(default='', verbose_name='Email')

    def __str__(self):
        return self.first_name + ' '+ self.last_name

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'


    #def charge(self) -> float:
        #self.price = self.col_of_ankself.price_ank + self.col_of_childself.price_child
        #return self.price

