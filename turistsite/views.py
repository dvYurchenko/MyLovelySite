from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from turistsite.models import MyTour


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