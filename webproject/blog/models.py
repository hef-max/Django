from django.db import models

# Create your models here.

class Posts(models.Model):
	title = models.CharField(max_length=250)
	body = models.TextField()
	# coba = models.
	def __str__(self):
		return "{}".format(self.title)
		