# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post,Profile
from . import models

# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)