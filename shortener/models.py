from django.db import models
from django.contrib.auth.models import User

class Link(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	url = models.URLField(unique=True)
	short_code = models.URLField(unique=True)
	title = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)
	image = models.URLField(blank=True, null=True)
	views_count = models.PositiveIntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	destroyed_at = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.short_url