from django.db import models

# Create your models here.

class Place(models.Model):
	name = models.CharField(max_length=200) #limits characters to 200
	visited = models.BooleanField(default=False) #assigns boolean to see if this place has been visited
	
	def __str__(self):
		return '%s visited? %s' %(self.name, self.visited) #looks to see if location has been visited