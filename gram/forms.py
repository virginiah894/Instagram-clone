from django import forms
from .models import Post,Profile,Comment
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from  crispy_forms.layout import Submit,Layout,Field


class UserPostForm(forms.ModelForm):
  helper =FormHelper()
  helper.form_method ='POST'
  helper.add_input(Submit('Post','Post',css_class='btn-primary'))
  class Meta:
     model = Post
     fields =[
       'image',
       'caption'
     ]
  def save(self,commit=True):
    user = super().save(commit=False)
    if commit:
      user.save()
    return user

# class UserPostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         exclude = ['author', 'posted_date','comments','likes']
       
class DetailsUpdate(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['profile_photo','bio']  

class CommentPostForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user','post','comment_on']
    
     

    
class AccountUpdate(forms.ModelForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ['username','email']
