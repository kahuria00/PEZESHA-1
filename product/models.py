from django.db import models

class Product(models.Model):
	product_name=models.CharField(max_length=30)
	product_description=models.CharField(max_length=100)
	

def __str__(self):
	return self.product_name

# Create your models here.
