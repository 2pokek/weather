from django.shortcuts import render
import requests

def index(request):
    appid = '9bf0385f33a4eeb5ba2bf7dcd7896c69'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid
    city= 'Minsk'
    res = requests.get(url.format(city))
    print(res.text)

    return render(request,'weather/index.html')

def asd(request):
    return render(request,'weather/asd.html')
