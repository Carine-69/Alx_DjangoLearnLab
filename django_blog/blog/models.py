from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.

# Capitalize the class name 'Post'
class Post(models.Model):  
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.TimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(tag, related_name='post', blank=True)

    def __str__(self):
        return self.title

# Comment model with correct foreign key reference
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

class tag(models.Model):
	name = models.ChaField(max_length=100, unique=True)

	def __str__(self):
		return self.name
