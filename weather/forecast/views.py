from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def index(request):
    appid = '9bf0385f33a4eeb5ba2bf7dcd7896c69'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm

    cities = City.objects.all()

    all_cities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"],
            'feel': res["main"]["feels_like"],

        }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)


def asd(request):
    return render(request, 'weather/asd.html')
