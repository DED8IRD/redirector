from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class URL(models.Model):
	url = models.URLField(unique=True)
	code = models.CharField(max_length=50, primary_key=True)
	created_date = models.DateTimeField(default=timezone.now)
	access_count = models.IntegerField(default=0)

	def __str__(self):
		return f'{self.url}-{self.code}'


class UserSavedLink(models.Model):
	url = models.ForeignKey(URL, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.url}'	
