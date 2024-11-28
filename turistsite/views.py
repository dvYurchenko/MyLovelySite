from lib2to3.fixes.fix_input import context

from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import get_template

from turistsite.models import MyTour, Booking1  # , Booking
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm, ContactForm  , MyBooking
from django.contrib import messages


def home(request):
    return render(request, 'index.html')

def first(request):
    tur_PERM = MyTour.objects.filter (type__exact = "PERM")
    tur_URAL = MyTour.objects.filter(type__exact="URAL")
    tur_ACT = MyTour.objects.filter(type__exact="ACT")
    tur_CHILD = MyTour.objects.filter(type__exact="CHILD")
    context={'tur_PERM':tur_PERM, 'tur_URAL':tur_URAL, 'tur_ACT':tur_ACT, 'tur_CHILD':tur_CHILD}
    return render(request, 'first.html', context=context)

def second(request):
    tur_PERM = MyTour.objects.filter (type__exact = "PERM")
    tur_URAL = MyTour.objects.filter(type__exact="URAL")
    tur_ACT = MyTour.objects.filter(type__exact="ACT")
    tur_CHILD = MyTour.objects.filter(type__exact="CHILD")
    context={'tur_PERM':tur_PERM, 'tur_URAL':tur_URAL, 'tur_ACT':tur_ACT, 'tur_CHILD':tur_CHILD}
    return render(request, 'second.html', context=context)

def third(request):
    tur_PERM = MyTour.objects.filter (type__exact = "PERM")
    tur_URAL = MyTour.objects.filter(type__exact="URAL")
    tur_ACT = MyTour.objects.filter(type__exact="ACT")
    tur_CHILD = MyTour.objects.filter(type__exact="CHILD")
    context={'tur_PERM':tur_PERM, 'tur_URAL':tur_URAL, 'tur_ACT':tur_ACT, 'tur_CHILD':tur_CHILD}
    return render(request, 'third.html', context=context)

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()          # Сохраняем нового пользователя
            login(request, user)        # Выполняем вход
            return redirect('home')     # Перенаправляем на главную страницу
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    form = LoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password) # Проверяем учетные данные
            if user is not None:
                login(request, user)     # Выполняем вход
                return redirect('home')  # Перенаправляем на главную страницу
    return render(request, 'login.html', {'form': form})

def sign_out(request):
    logout(request)
    messages.success(request, 'Вы вышли из аккаунта')
    return redirect('home')

def contacts(request):
    context={}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['message'])
            context={'success':1}
    else:
        form=ContactForm()
    context['form']=form
    return render(request, 'contacts.html', context=context)

def about(request):
    return render(request, 'about.html')

def send_message(name, email, message):
    text=get_template('message.html')
    html = get_template('message.html')
    context = {'name': name, 'email':email, 'message':message}
    subject = 'Сообщение от пользователя'
    from_email='turist@example.com'
    text_content = text.render(context)
    html_content = html.render(context)

    msg=EmailMultiAlternatives(subject, text_content, from_email, ['yurchenko.dasha13@gmail.com'])
    msg.attach_alternative(html_content,'text/html')
    msg.send()

def booking(request):
    #model = MyBooking.objects.all()
    #fields =["first_name", "last_name", "title_of_trip", "col_of_ank", "col_of_child", "price_ank", "price_child", "checkin_date", "email", " price"]

    if request.method == 'POST':
        form = MyBooking(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем нового пользователя
            return redirect('home')  # Перенаправляем на главную страницу
    else:
        form = MyBooking()

    return render(request, 'booking.html', {'form': form}) #, 'model':model,'fields':fields})