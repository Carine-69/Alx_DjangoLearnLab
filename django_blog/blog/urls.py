from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.models import User

class form(UserCreationForm):
	email = forms.EmailField(required=True)

	class meta:
		model=User
		fields = ('username','email','password1','passwird2')
