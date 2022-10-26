from django.shortcuts import render

def index(request):
    return render(request,'weather/index.html')

def asd(request):
    return render(request,'weather/asd.html')
