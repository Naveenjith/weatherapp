from django.shortcuts import render
import requests
from .models import WeatherData

def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'London'
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=583a1e0afcada769555b94799c23d3e0'
    params = {'units': 'metric'}
    data = requests.get(url, params=params).json()

    if data.get('cod') != '404':
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        humidity = data['main']['humidity']

        # for saving data to database
        weather = WeatherData(
            city=city,
            description=description,
            temperature=temp,
            humidity=humidity,
            icon=icon,
            
        )
        weather.save()

        # Alert if weather condition is extreme
        extreme_alert = None
        if temp > 40 or temp < 0 or humidity > 90:
            extreme_alert = "Extreme weather condition!"

        return render(request, 'index.html', {
            'description': description,
            'icon': icon,
            'temp': temp,
            'city': city,
            'extreme_alert': extreme_alert,
            'humidity': humidity,
            'day': weather.date
        })
    else:
        return render(request, 'index.html', {'error': 'City not found'})

