from django.shortcuts import render,redirect
import requests
import datetime

API_KEY='a7862b100cf135a8d3685996ca8497b3'
LANG='tr'
def index(request):
    q = request.GET.get('q')
    if q == '':
        return redirect('home')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={q}&units=metric&lang={LANG}&appid={API_KEY}'
    response = requests.get(url).json()
    if response['cod'] == '404':
        error = 'Şehir Bulunamadı.'
        return render(request,'index.html',{'error':error})
    print(response)
    context = {
        'description':response['weather'][0]['description'],
        'city':response['name'],
        'temp':round(response['main']['temp']),
        'min_temp':round(response['main']['temp_min']),
        'max_temp':round(response['main']['temp_max']),
        'feels_like':round(response['main']['feels_like']),
        'wind':response['wind']['speed'],
        'humidity':response['main']['humidity'],
        'dt': datetime.datetime.fromtimestamp(response['dt']),
        'icon_url': f"http://openweathermap.org/img/wn/{response['weather'][0]['icon']}.png",
        'q':q
    }

    return render(request, 'index.html', context)
