from django.db import models

class User(models.Model):
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=30)
	email=models.EmailField()
	password=models.CharField(max_length=15)
	confirm_password=models.CharField(max_length=15)

def __str__(self):
	return self.first_name+"  "+self.last_name

# Create your models here.
