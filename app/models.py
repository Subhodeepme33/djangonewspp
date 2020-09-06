from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	password=models.CharField(max_length=50)
	dob= models.DateField()
	blogcount=models.IntegerField()

	def __str__(self):
		return self.name

	class Meta:
		db_table = "users"