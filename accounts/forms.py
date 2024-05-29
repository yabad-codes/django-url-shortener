from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']
		widgets = {
			'username': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Username'}),
		}
	
	def __init__(self, *args, **kwargs):
		super(SignupForm, self).__init__(*args, **kwargs)
		self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Password'})
		self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Confirm Password'})

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Password'})
    )