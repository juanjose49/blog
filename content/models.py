from django.db import models

# Create your models here.

class PubType(models.Model):
	type = models.CharField(max_length=200)

	def __str__(self):
		return self.type

class Publication(models.Model):
	type = models.ForeignKey(PubType, default=None)
	date = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=200)
	content = models.TextField(default='')
	img = models.CharField(max_length=200)

	def __str__(self):
		return self.title

class StaticContent(models.Model):
	purpose = models.CharField(max_length=200)
	content = models.TextField(default='')

	def __str__(self):
		return self.purpose

	

