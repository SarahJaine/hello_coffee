from django.db import models

# Create your models here.
class Shop(models.Model):
	name = models.CharField(max_length=255)
	description =  models.TextField()
	slug = models.SlugField(unique=True)
	zip_code = models.IntegerField()