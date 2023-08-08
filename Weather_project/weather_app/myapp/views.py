from asyncore import read
import imp
from django.http import HttpResponse
from django.shortcuts import render
import urllib.request
import json

import urllib3


# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=b43ef4b8ebacd7a33a9655d447d341c2")
        res_ = res.read()
        json_data = json.loads(res_.decode('utf-8'))
        data = {
            'country_code':str(json_data['sys']['country']),
            'coordinate':str(json_data['coord']['lon']) + ' '
            +str(json_data['coord']['lat']),
            'temp':str(round(int(int(json_data['main']['temp'])-273.15),1)) + '°C',
            'pressure':str(json_data['main']['pressure']),
            'humidity':str(json_data['main']['humidity'])
        }
    else:
        city = ''
        data= {}
    return render(request,'index.html',{'city':city,'data':data})

    # https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}