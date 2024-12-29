from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .models import post
# Create your models here.

class post(models.Model):
	title=models.CharField(max_length=200)
	content=models.TextField()
	published_date=models.TimeField(auto_now_add=True)
	author=models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.title

class comment(models.Model):
	post = models.ForeignKey(post, related_name='comments', on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'comment by {self.author} on {self.post}'
