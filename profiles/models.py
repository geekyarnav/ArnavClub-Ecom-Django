from __future__ import unicode_literals
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=120)
    desc = models.TextField(default="Enter the Description",max_length=500)
    location = models.CharField(max_length=120,default='Default : Delhi')
    job = models.CharField(max_length=120,null = True)
    
def __unicode__(self):
    return self.name


# New Contact Bug Fix

# class Contact(models.Model):
#     email = models.EmailField()
#     subject = models.CharField(max_length=255)
#     message = models.TextField()

#     def __str__(self):
#         return self.email
# # ADD
# class BlogArticle (models.Model):
#     #fields
#     title = models.CharField(max_length=100)
#     blog_content = models.TextField(max_length=500)
#     Users = get_user_model()
#     #author = models.ForeignKey(Users)#---------------------[PROBLEM]
