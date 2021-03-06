# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404,redirect
from .models import Post,Profile,Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from .forms import  UserPostForm,AccountUpdate,DetailsUpdate,CommentPostForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.views.generic import(
  ListView,
  CreateView,
  DetailView,

)

# Create your views here.
# @login_required(login_url='/accounts/login/')
class PostListView(LoginRequiredMixin,ListView):
  template_name = 'gram/post_list.html'
  queryset = Post.objects.all()[::-1]
  context_object_name ='posts'
  class Meta:
    ordering = ['posted_date']

# @login_required(login_url='/accounts/login/')
# class PostCreateView(LoginRequiredMixin,CreateView):
#   template_name = 'gram/create.html'
#   form_class = PostForm
#   queryset = Post.objects.all()
#   success_url = '/' 

#   def form_valid(self,form):
#      print (form.cleaned_data)
#      form.instance.author = self.request.user
#      form.save()
#      return super().form_valid(form)

# @login_required(login_url='/accounts/login/')



def post_comment(request,id):

    current_user = request.user
    post = Post.get_one_post(id=id)
    if request.method == 'POST':
        form = CommentPostForm(request.POST)
        print(form)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.post_id = id
            comment.save()
        return redirect('/')

    else:
        form = CommentPostForm()
        return render(request,'gram/post_comment.html',{"form":form,"post":post})  
    
def all_comments(request,id):
    comments = Comment.all_comments(id)
    number = len(comments)
    
    return render(request,'gram/comment.html',{"comments":comments,"number":number})   

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
def new_post(request,id):
    current_user = request.user
    if request.method == 'POST':
        form = UserPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = current_user
            post.save()
        return HttpResponseRedirect('/')

    else:
        form =UserPostForm()
    return render(request, 'gram/create.html', {"form": form})


@login_required
def account_update(request):
  
  # if request.method == 'POST':
  #   try:
  #     profile = request.user.profile
  #   except Profile.DoesNotExist:
  #     profile = Profile(user=request.user)
  if request.method == 'POST':
       user_form = AccountUpdate(request.POST,instance=request.user)
       details_form = DetailsUpdate(request.POST ,request.FILES,instance=request.user.profile)
       if user_form.is_valid() and details_form.is_valid():
          user_form.save()
          details_form.save()
          messages.success(request,f'Your Profile account has been updated successfully')
          return redirect('gram:profile')
  else:
  

      user_form = AccountUpdate(instance=request.user)
      
      details_form = DetailsUpdate(instance=request.user.profile) 
  forms = {
    'user_form':user_form,
    'details_form':details_form
  }
  return render(request,'gram/update_info.html',forms)




@login_required
def profile(request):
  current_user = request.user
  
  profile = Profile.objects.get_or_create(user=request.user)
  images = request.user.post_set.all()
  
  post = images.count()
  
  
  return render(request,'gram/profile.html',{"profile":profile,'images':images,"post":post})
