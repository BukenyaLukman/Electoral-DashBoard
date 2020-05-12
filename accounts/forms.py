from django.forms import ModelForm
from .models import *

class ConstituencyForm(forms.ModelForm):
	class Meta:
		model = Constituency
		fields = '__all__'