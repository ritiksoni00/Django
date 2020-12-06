from django.shortcuts import render
from django.http import HttpResponse
from dashboard.forms import CityForm
from dashboard.models import City
from dashboard.helper_view import get_wthr_data


def home(request):
	form = CityForm()
	
	if request.method == 'POST': 
		form=CityForm(request.POST)

		if form.is_valid():
			form.save()
			city_name =form.cleaned_data.get('city_name')
			weather_data=get_wthr_data(city_name)
	elif request.method =='GET':
		city_name=City.objects.latest('date_added').city_name
		weather_data=get_wthr_data(city_name)

	context={'form': form, 'weather_data': weather_data}
	return render(request, 'home.html', context=context)




def history(request):
	template='history.html'
	cities=City.objects.all().order_by('-date_added')[:5]
	data_list=[]
	for city in cities:
		city_name=city.city_name
		data_list.append(get_wthr_data(city_name))
		
	context={'data_list': data_list}
	return render(request, template, context)