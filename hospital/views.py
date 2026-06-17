from django.shortcuts import render


def inicio(request):
    return render(request, 'sesion.html')

def home(request):
    return render(request, 'index.html')

