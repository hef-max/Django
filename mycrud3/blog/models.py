from django.db import models

# Create your models here.
class PostModel(models.Model):
	nim 	= models.CharField(max_length=20)
	nama 	= models.CharField(max_length=20)
	LIST_CATEGORY = (
		('Perempuan', 'Perempuan'),
		('Laki-Laki', 'Laki-Laki'),
	)
	jk	= models.CharField(
		max_length=20,
		choices=LIST_CATEGORY,
		default= 'Laki-Laki',
	)
	tanggal_lahir	= models.CharField(max_length=20)
	prodi 			= models.CharField(max_length=20)
	published		= models.DateTimeField(auto_now_add=True)
	updated			= models.DateTimeField(auto_now=True)

	def __str__(self):
		return "{}. {}".format(self.id, self.judul)