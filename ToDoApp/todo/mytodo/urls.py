from django.urls import path
from mytodo.views import home, add_todo
from django.contrib import admin

urlpatterns = [
		path('admin', admin.site.urls),
		path('', home, name='home'),
		path('add_todo/', add_todo, name='add_todo')

]