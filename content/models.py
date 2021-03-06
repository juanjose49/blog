from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class PubType(models.Model):
	type = models.CharField(max_length=200)

	def __str__(self):
		return self.type

class Publication(models.Model):
	type = models.ForeignKey(PubType, default=None)
	date = models.DateTimeField()
	title = models.CharField(max_length=200)
	content = RichTextField()
	short_content = models.TextField(default='')
	img = models.ImageField(upload_to='img/')

	def __str__(self):
		return self.title

class StaticContent(models.Model):
	purpose = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	content = models.TextField(default='')
	img = models.ImageField(upload_to='img/')


	def __str__(self):
		return self.purpose

	

