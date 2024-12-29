from .models import comment
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.models import User

class CreationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model=User
		fields = ('username','email','password1','password2')

class commentForm(forms.ModelForm):
	class Meta:
		model = comment
		fields = ['comment']
