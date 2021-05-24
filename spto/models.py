from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, blank=True)
	birth_date = models.DateField(null=True, blank=True)

class Article(models.Model):
	title = models.CharField('제목', max_length=126, null=False)
	content = models.TextField('내용', null=False)
	author = models.CharField('작성자', max_length=16, null=False)
	created_at = models.DateTimeField('작성일', auto_now_add=True)


# Create your models here.
