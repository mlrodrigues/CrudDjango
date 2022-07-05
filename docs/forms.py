from django import forms
from .models import Docs

class docsForms(forms.ModelForm):
	class Meta:
		model = Docs
		fields = '__all__'