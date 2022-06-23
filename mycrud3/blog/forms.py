from django import forms
from .models import PostModel

class PostForm(forms.ModelForm):
	class Meta:
		model = PostModel
		fields = [
			"nim",
			"nama",
			"jk",
			"tanggal_lahir",
			"prodi",
		]