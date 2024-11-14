from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Обязательное поле. Введите действующий email.')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

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

    #def clean_username(self):
        #username = self.cleaned_data.get('username')
        #if ' ' in username:
            #raise forms.ValidationError("Не должно быть пробелов")
        #return username

    #def clean(self):
        #cleaned_data = super().clean()
        #password = cleaned_data.get('password1')
        #confirm_password = cleaned_data.get('password2')

        #if password != confirm_password:
            ##raise forms.ValidationError("Пароли не совпадают")

#class LoginForm(AuthenticationForm):
    #username = forms.CharField(label='Имя пользователя')
    #password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

