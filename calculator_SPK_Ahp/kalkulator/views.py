from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Halo, ini halaman utama!")

def about(request):
    return HttpResponse("Ini halaman About!")

def spk_ahp(request):
    return HttpResponse("Ini halaman kalkulator SPK AHP!")
