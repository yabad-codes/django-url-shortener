from django.db import models
from django.contrib.auth.models import User
from .base62 import base62_encode
from django.utils import timezone
from datetime import timedelta
from bs4 import BeautifulSoup
import requests

class Link(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	url = models.URLField(unique=True)
	short_code = models.CharField(max_length=10, unique=True)
	title = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)
	image = models.URLField(blank=True, null=True)
	views_count = models.PositiveIntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	destroyed_at = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.short_url
	
	def fetch_metadata(self):
		try:
			response = requests.get(self.url)
			response.raise_for_status()
			soup = BeautifulSoup(response.text, 'html.parser')

			# Get title
			if not self.title:
				title_tag = soup.find('title')
				self.title = title_tag.string if title_tag else self.url
			
			# Get description
			if not self.description:
				description_tag = soup.find('meta', attrs={'name': 'description'})
				if description_tag and 'content' in description_tag.attrs:
					self.description = description_tag['content']
				else:
					self.description = 'No description found'
			
			# Get favicon
			if not self.image:
				favicon_tag = soup.find('link', rel='icon')
				if not favicon_tag:
					favicon_tag = soup.find('link', rel='shortcut icon')
				if favicon_tag and 'href' in favicon_tag.attrs:
					favicon_url = favicon_tag['href']
					if favicon_url.startswith('/'):
						from urllib.parse import urljoin
						favicon_url = urljoin(self.url, favicon_url)
					self.image = favicon_url
			else:
				self.image = ''
		except requests.RequestException as e:
			print(f"Error fetching metadata for URL {self.url}: {e}")
		pass

	def save(self, *args, **kwargs):
		if not self.pk:
			self.fetch_metadata()
		super().save(*args, **kwargs)
		if not self.short_code:
			self.short_code = base62_encode(self.pk)
			super().save(*args, **kwargs)
		
		if not self.destroyed_at:
			if self.user is None:
				self.destroyed_at = timezone.now() + timedelta(hours=1)
			else:
				self.destroyed_at = timezone.now() + timedelta(days=365)
			super().save(*args, **kwargs)