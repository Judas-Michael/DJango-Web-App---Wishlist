from django import forms
from .models import Place

class NewPlaceForm(forms.ModelForm):
	class Meta: 
		model = Place
		fields = ('name', 'visited')
		
		#This adds the form to fill out. Where did you visit and has it been visited