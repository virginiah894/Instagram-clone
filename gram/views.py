# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.views.generic import(
  ListView,
  CreateView,
)

# Create your views here.
class PostListView(ListView):
  template_name = 'gramm/all posts.html'
  queryset = Post.objects.all()
  context_object_name ='posts'

class PostCreateView(CreateView):
  template = 'gramm/create.html'
  form = PostForm()
  queryset = Post.objects.all()
  success_url = '/' 

  def form_valid(self):
     print (form.cleaned_data)
     form.instance.author = self.request.user
     return super().form_valid(form)

