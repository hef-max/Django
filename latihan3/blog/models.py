from django.db import models

# Create your models here.


class Post(models.Model):
	"""docstring for Post"""
	title = models.CharField(max_length=200)
	body = models.TextField()
	email = models.EmailField(default='name@web.com')
	alamat = models.CharField(max_length=200, blank=True)
	waktu = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return "{} {}".format(self.title, self.waktu)
		