# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from tinymce.models import HTMLField
from PIL import Image
from django.db.models.signals import post_save
from django.db import models
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    
    profile_photo = models.ImageField(default='fur.jpg', upload_to='profile_pics')
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=250)
    follows = models.ManyToManyField('Profile', related_name='followed_by')


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args,**kwargs):
        super().save()
        
        img = Image.open(self.profile_photo.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_photo.path)

    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)

    #         post_save.connect(create_user_profile, sender=User)



class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    caption = HTMLField(null=True)
    posted_date = models.DateTimeField(default=timezone.now)
    # comments = HTMLField(null=True)
    likes = models.TextField(null=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)


    @classmethod
    def search_by_author(cls,search_term):
        posts = cls.objects.filter(profile__icontains=search_term)
        return posts


    def __str__(self):
      return self.caption

    @classmethod
    def get_one_post(cls,id):
        post = cls.objects.get(pk=id)
        return post


    @classmethod
    def all_posts(cls):
        posts = cls.objects.all()
        return posts


    def save_post(self):
        super().save()
    def delete_post(self):
        return self.delete()

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    comment = models.CharField(max_length=230,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    commented_on = models.DateTimeField(auto_now_add=True)

    def save_comment(self):
        self.save()
    
    
    @classmethod
    def all_comments(cls,id):
        comments = cls.objects.filter(post__id=id)
        return comments
    
    
    def __str__(self):
        
        return self.comment
        
    
     