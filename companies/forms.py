from django import forms
from .models import Companies
from users.models import Users

LANGUAGES = [('PT', 'PT'), ('ES', 'ES'), ('EN', 'EN')]

class companiesForms(forms.ModelForm):
	class Meta:
		model = Companies
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(companiesForms, self).__init__(*args, **kwargs)
		self.fields['lang'] = forms.ChoiceField(widget=forms.RadioSelect, choices=LANGUAGES)