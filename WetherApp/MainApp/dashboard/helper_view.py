from django.conf import settings
# Create your views here.
import requests


def get_wthr_data(city_name):
	url='https://api.openweathermap.org/data/2.5/weather'
	
	params = {
				'q': city_name,
				'appid' : settings.OWA_APY_KEY,
				'units' : 'metric',
	}	
	res=requests.get(url, params=params)

	if res.status_code != 200:
		return None



	json_res=res.json()
	weather_data ={
					'temp': json_res['main']['temp'],
					'temp_min': json_res['main']['temp_min'],
					'temp_max': json_res['main']['temp_max'],
					'city_name': json_res['name'],
					'country': json_res['sys']['country'],
					'lat': json_res['coord']['lat'],
					'lon': json_res['coord']['lon'],
					'weather': json_res['weather'][0]['main'],
					'weather_desc': json_res['weather'][0]['description'],
					'pressure': json_res['main']['pressure'],
					'humidity': json_res['main']['humidity'],
					'wind_speed': json_res['wind']['speed'],
				}
	return weather_data