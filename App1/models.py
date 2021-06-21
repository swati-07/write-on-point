from django.db import models
from django.utils import timezone
from django.shortcuts import redirect,render,reverse

# Create your models here.
class Blog(models.Model):
	author=models.CharField(max_length=20)
	title =models.CharField(max_length=30)
	blog = models.TextField()
	caption=models.CharField(max_length=100)
	photo1=models.ImageField(upload_to='images/')
	photo2=models.ImageField(upload_to='images/')
	starttime=models.DateTimeField(auto_now_add=True)
	published=models.BooleanField(default=False)
	publishtime=models.DateTimeField(null=True)
	
	def publish(self):
		
		return reverse(viewname='publish',kwargs={'pk':self.pk})

	def deletepost(self):
		
		return reverse(viewname='delete',kwargs={'pk':self.pk})