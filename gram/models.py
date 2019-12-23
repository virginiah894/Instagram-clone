# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Author(models.Model):
    first_name = models.TextField(max_length=100)

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    caption = models.TextField()
    posted_date = models.DateTimeField(default=timezone.now)
     
    def __str__(self):
      return self.caption