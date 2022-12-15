from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    appid = 'e4f24cdbf69bf7451a582f26b2b238f0'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid="+appid

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'humidity': res["main"]["humidity"],
            'speed': res["wind"]["speed"],
            'icon': res["weather"][0]["icon"],
        }
        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form }
    return render(request, 'weather\index.html', context)

def home(request):
    appid = 'e4f24cdbf69bf7451a582f26b2b238f0'
    url = "https://api.openweathermap.org/data/2.5/weather?q=Brest&units=metric&appid=" + appid
    city = 'Брест'
    res = requests.get(url.format(city)).json()
    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"],
        'humidity': res["main"]["humidity"],
        'speed': res["wind"]["speed"],
    }

    context = {'info': city_info}
    return render(request, 'weather\home.html', context)
