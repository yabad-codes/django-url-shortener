from django import forms
from .models import Link

class LinkForm(forms.ModelForm):
	class Meta:
		model = Link
		fields = ['url']
		widgets = {
			'url': forms.URLInput(attrs={'class': 'input-url', 'placeholder': 'https://example.com'}),
		}