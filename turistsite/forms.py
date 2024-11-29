from datetime import timezone, datetime

from ckeditor import widgets
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
#from models import Booking1
from rest_framework import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from turistsite.models import Booking1, MyTour
from django.forms import ModelForm, DateInput, DateTimeField, DateField


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(max_length=100, label='Имя', widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}))
    last_name = forms.CharField(max_length=100, label='Фамилия', widget=forms.TextInput(attrs={'placeholder': 'Ваша фимилия'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name.lower().find(" ") != -1:
            raise forms.ValidationError("Имя не должно содержать пробелы.")
        return first_name

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

class ContactForm(forms.Form):
    name=forms.CharField(min_length=2, widget=forms.TextInput(attrs={'placeholder': 'Ваше имя', 'class':'form_control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class':'form_control'}))
    message=forms.CharField(min_length=5, widget=forms.Textarea(attrs={'placeholder': 'Сообщение','col':30, 'rows': 9, 'class':'form_contr_1'}))

class MyBooking(forms.ModelForm):
    checkin_date = forms.DateField(widget=DateInput(attrs={'type': 'date'}), label='Дата поездки')

    class Meta:
         model = Booking1
         fields =["first_name", "last_name", "title_of_trip", "col_of_ank", "col_of_child", "checkin_date", "email"]

#class SignUpForm(UserCreationForm):
    #name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Вашя имя'}))
    #password1 = forms.CharField(min_length=8, widget=forms.PasswordInput)
    #password2 = forms.CharField(min_length=8, widget=forms.PasswordInput)
    #email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    #phone_number = forms.CharField(max_length=15, widget=forms.NumberInput(attrs={'placeholder': 'Телефон'}))
    #birthday = forms.DateField()
    #second_name = forms.CharField(max_length=30, help_text='Отчество')
    #surname = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Вашя фамилия'}))
    #class Meta:
        #model = User
        #fields = ('username', 'second_name', 'surname', 'birthday', 'email', 'phone_number', 'password1', 'password2')



    #def clean(self):
        #cleaned_data = super().clean()
        #password = cleaned_data.get('password1')
        #confirm_password = cleaned_data.get('password2')

        #if password != confirm_password:
            ##raise forms.ValidationError("Пароли не совпадают")

#class LoginForm(AuthenticationForm):
    #username = forms.CharField(label='Имя пользователя')
    #password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

