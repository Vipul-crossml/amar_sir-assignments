from django import forms
from django.forms import ModelForm

from .models import *


class ExpenseForm(forms.ModelForm):
	title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add expense...'}))

	class Meta:
		model = Category
		fields = '__all__'