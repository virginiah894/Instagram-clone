# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.views.generic import(
  ListView,
  CreateView,
  DetailView,
)

# Create your views here.
class PostListView(ListView):
  template_name = 'gram/all posts.html'
  queryset = Post.objects.all().filter(posted_date__lte=timezone.now()).order_by('-posted_date')
  context_object_name ='posts'

class PostCreateView(CreateView):
  template_name = 'gram/create.html'
  form_class = PostForm
  queryset = Post.objects.all()
  success_url = '/' 

  def form_valid(self,form):
     print (form.cleaned_data)
     form.instance.author = self.request.user
     return super().form_valid(form)

class PostDetailView(DetailView):
  queryset=Post.objects.all().filter(posted_date__lte=timezone.now())
  def get_object(self):
    id_=self.kwargs.get('id')
    return get_object_or_404(Post,id=id_)
    template_name = 'gram/post_detail.html'