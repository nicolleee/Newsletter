from django.http import HttpResponse
from django.shortcuts import render


def homep(request):
    return render(request, 'home.html')


def participantip(request):
    return render(request, 'participanti.html')
