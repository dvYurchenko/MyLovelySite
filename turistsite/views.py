from django.shortcuts import render
from turistsite.models import MyTour, Booking
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm#, MyBooking
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

#def booking(request):
    #if request.method == 'POST':
        #form = MyBooking(request.POST)
        #if form.is_valid():
            #form.save()  # Сохраняем нового пользователя
            #return redirect('home')  # Перенаправляем на главную страницу
    #else:
        #form = MyBooking()
    #return render(request, 'booking.html', {'form': form})