# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Post, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from .forms import PostForm, UserPostForm
from django.http import HttpResponse
from django.views.generic import(
  ListView,
  CreateView,
  DetailView,

)

# Create your views here.
# @login_required(login_url='/accounts/login/')
class PostListView(LoginRequiredMixin,ListView):
  template_name = 'gram/post_list.html'
  queryset = Post.objects.all().filter(posted_date__lte=timezone.now()).order_by('-posted_date')
  context_object_name ='posts'

# @login_required(login_url='/accounts/login/')
class PostCreateView(LoginRequiredMixin,CreateView):
  template_name = 'gram/create.html'
  form_class = PostForm
  queryset = Post.objects.all()
  success_url = '/' 

  def form_valid(self,form):
     print (form.cleaned_data)
     form.instance.author = self.request.user
     return super().form_valid(form)

# @login_required(login_url='/accounts/login/')

class PostDetailView(LoginRequiredMixin,DetailView):
  queryset=Post.objects.all().filter(posted_date__lte=timezone.now())
  def get_object(self):
    id_=self.kwargs.get('id')
    return get_object_or_404(Post,id=id_)
    template_name = 'gram/post_detail.html'
# searching view
@login_required(login_url='/accounts/login/')

def search_posts(request):
    if 'user' in request.GET and request.GET['user']:
      search_term = request.GET.get('user')
      searched_users = Post.search_by_author(search_term)
      message = f'{search_term}'
      return render (request, 'gram/search.html',{'message':message,'users':searched_users})
    else:
      message = "Nothing was searched.Please ensure you type something"
      return render (request, 'gram/search.html',{'message':message})


      # try different auth
@login_required
def account(request):
  return render (request,'account.html',{})      

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = UserPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = current_user
            post.save()
        return redirect('/')

    else:
        form =UserPostForm()
    return render(request, 'gram/create.html', {"form": form})


@login_required
def profile(request):
  current_user = request.user
  profile = Profile.objects.all()
  
  posts = Post.objects.all()
  
  
  return render(request,'gram/profile.html',{"profile":profile, "posts":posts})
