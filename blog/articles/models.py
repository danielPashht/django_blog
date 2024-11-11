from django.db import models


class TimeStampedModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		abstract = True


class Post(TimeStampedModel):
	author = models.CharField(max_length=100)
	title = models.CharField(max_length=100, null=True)
	content = models.TextField()
	updated_at = models.DateTimeField(null=True)

	def __str__(self):
		return self.title
