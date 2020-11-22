from django.shortcuts import render
from django.http import HttpResponse
from mytodo.models import ToDo
from mytodo.forms import todoform


# Create your views here.
def home(request):
	 todo_list = ToDo.objects.all()
	 form = todoform() 
	 context={'app_name' : 'ToDo App', 'todo_list' : todo_list ,'form' : form}
	 return render(request, 'index.html' , context=context)
	


def add_todo(request):
	if request.method == 'POST':
		print(request.POST)
		return HttpResponse('iui')