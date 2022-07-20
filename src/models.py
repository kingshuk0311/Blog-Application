from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaEditor
from .helpers import *


class BlogModel(models.Model):
    title=models.CharField(max_length=100)
    pcontent=models.TextField()
    #content=models.FroalaField()
    slug=models.SlugField(max_length=1000,null=True,blank=True)
    image=models.ImageField(upload_to='blog')
    created_at=models.DateTimeField(auto_now_add=True)  #it is fixed whenever blog created
    upload_to=models.DateTimeField(auto_now=True)  #whenever model will call it will update


    def __str__(self):
        return self.title
 

     # This is function overloading  
    def save(self,*args,**kwargs):
        self.slug=generate_slug(self.title)
        super(BlogModel,self).save(*args,**kwargs)




# Create your models here.
