import requests
from django.shortcuts import render
from .models import Clima

def clima(request):
    ciudades = ['Rosario', 'Buenos Aires', 'Córdoba']
    api_key = 'b629060f62d09536da90e839384b7929'
    climas = []
    
    for ciudad in ciudades:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric'
        response = requests.get(url).json()
        print(response)
        if 'main' in response:
            temperatura = response['main']['temp']
        else:
            temperatura = None

        if 'weather' in response:
            descripcion = response['weather'][0]['description']
            icono = response['weather'][0]['icon']
        else:
            descripcion = None
            icono = None

        clima = Clima(ciudad=ciudad, temperatura=temperatura, descripcion=descripcion, icono=icono)
        clima.save()

    for ciudad in ciudades:
        clima = Clima.objects.filter(ciudad=ciudad).order_by('-id').first()
        climas.append(clima)

    return render(request, 'clima.html', {'climas': climas})


def acerca(request):
    return render(request, 'acerca.html')

def contacto(request):
    return render(request, 'contacto.html')