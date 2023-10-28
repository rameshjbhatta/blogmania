"""Hello from models"""
from django.db import models
from django.urls import reverse

class BlogInfo(models.Model):
   title = models.CharField(max_length=100)
   img=models.ImageField(null=True, upload_to='images')
   content =models.TextField()
   date_time=models.DateTimeField(auto_now_add=True)
   author=models.CharField(max_length=100)
   type=models.CharField(null=True , max_length=100)
   related_to=models.CharField(null=True,max_length=100)
  
   def __str__(self):
        return self.title

   def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
   
   
   class Meta:
          db_table='bloginfo'


class ContactInfo(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    message=models.TextField()
