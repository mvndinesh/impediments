from django.db import models

# Create your models here.
class List(models.Model):
	item = models.CharField(max_length = 200)
	completed = models.BooleanField(default = False)

	def __str__(self):
		return self.item + " | " + str(self.completed)

		#Create your models here.
class ListAllDefects(models.Model):
	issuename = models.CharField(max_length = 300)
	originator = models.CharField(max_length = 20)
	addinfo = models.CharField(max_length = 300)
	priority = models.CharField(max_length = 20)
	createddate = models.CharField(max_length = 30)
	expecteddate = models.DateField()
	oremailid = models.EmailField(max_length = 254) 
	status = models.CharField(max_length=20)
	sample = models.CharField(max_length=20)
	

	def __str__(self):
		return self.issuename + " | " + str(self.originator)

				#Create your models here.
class ListAllDefects1(models.Model):
	issuename = models.CharField(max_length = 300)
	originator = models.CharField(max_length = 20)
	addinfo = models.CharField(max_length = 300)
	priority = models.CharField(max_length = 20)
	createddate = models.CharField(max_length = 30)
	expecteddate = models.DateField()
	

	def __str__(self):
		return self.issuename + " | " + str(self.originator)

