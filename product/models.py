from django.db import models
from user.models import User

class Product(models.Model):
	product_name=models.CharField(max_length=30)
	product_description=models.CharField(max_length=100)
	product_image=models.ImageField()
	user=models.ForeignKey(User,on_delete=models.PROTECT)
	

def __str__(self):
	return self.product_name

# Create your models here.
