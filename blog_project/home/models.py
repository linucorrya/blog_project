from django.db import models

class interior(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='picture')
    cate=models.CharField(max_length=50)
    desc=models.TextField()
    author=models.CharField(max_length=50)
    date=models.DateField()
    
class interior1(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()
    date=models.DateField()
    

# class interior2(models.Model):
#     name=models.CharField(max_length=50)
#     img=models.ImageField(upload_to='picture')
 

# Create your models here.
