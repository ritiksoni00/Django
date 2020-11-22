from django import forms

class todoform(forms.Form):
	todo_text=forms.CharField()