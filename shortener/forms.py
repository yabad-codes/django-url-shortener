from django import forms
from .models import Link
from django.core.exceptions import ValidationError

class LinkForm(forms.ModelForm):
	class Meta:
		model = Link
		fields = ['url']
		widgets = {
			'url': forms.URLInput(attrs={'class': 'input-url', 'placeholder': 'https://example.com'}),
		}
	
	def clean_url(self):
		url = self.cleaned_data['url']
		if Link.objects.filter(user=self.instance.user, url=url).exists():
			raise ValidationError("This link already exists.")
		return url