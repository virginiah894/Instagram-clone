# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from tinymce.models import HTMLField

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    caption = HTMLField(null=True)
    posted_date = models.DateTimeField(default=timezone.now)
    comments = HTMLField(null=True)
    likes = models.TextField(null=True)
    @classmethod
    def search_by_author(cls,search_term):
        posts = cls.objects.filter(author__icontains=search_term)
        return posts


    def __str__(self):
      return self.caption
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #CASCADE means if the user is deleted then delete the profile 
    profile_photo = models.ImageField(default='default_avatar.jpg', upload_to='profile_pics')
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=250)
    follows = models.ManyToManyField('Profile', related_name='followed_by')


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args,**kwargs):
        super(Profile,self).save(*args,**kwargs)
        
        img = Image.open(self.profile_photo.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_photo.path)
