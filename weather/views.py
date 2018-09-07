from django.shortcuts import render
import requests
# Create your views here.
def weather_view(request):
	url = 'http://api.openweathermap.org/data/2.5/find?q={}&units=imperial&appid=082c68e081c87691c85380998e4d0d6d'
	city = 'London'
	if request.method == 'POST':
		city = request.POST['city']
	data = requests.get(url.format(city)).json()
	# description = data['list'][0]['weather'][1]['description']

	city_weather = {
		'city': city,
		'temp': data['list'][0]['main']['temp'],
		'humidity': data['list'][0]['main']['humidity'],
		# 'description': description,
	}
	context = {'city_weather': city_weather}
	# print(city_weather)
	return render(request, 'weather/weather.html', {"city_weather": city_weather})
