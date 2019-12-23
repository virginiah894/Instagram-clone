# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Post(models.Model)
poster=models.ForeignKey('auth-user',on_delete=models.CASCADE)
image = models.ImageField(null=True)
caption = models.TextField()
posted_date = models.DateTimeField(default=timezone.now