from django.db import models
from articles.models import TimeStampedModel
from articles.models import Post
from django.conf import settings


class Comment(TimeStampedModel):
	post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	content = models.TextField()

	def __str__(self):
		return f'Commented by {self.author} on {self.post}'
