from django.db import models

# Create your models here.
class project(models.Model):
    title=models.CharField(max_length=200,null=True,blank=True)
    description=models.CharField(max_length=400,null=True,blank=True)
    featured_image=models.ImageField(null=True,blank=True)
    tag=models.ManyToManyField('Tag')
    demolink=models.CharField(max_length=200,null=True,blank=True)
    sourcecode=models.CharField(max_length=200,null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class review(models.Model):
  
    project=models.ForeignKey(project,on_delete=models.CASCADE,null=True,blank=True)
    body=models.CharField(max_length=500,null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)

class Tag(models.Model):
    name=models.CharField(max_length=400)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

