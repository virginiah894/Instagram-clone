from django import forms
from .models import Post
from crispy_forms.helper import FormHelper
from  crispy_forms.layout import Submit,Layout,Field


class PostForm(forms.ModelForm):
  helper =FormHelper()
  helper.form_method ='POST'
  helper.add_input(Submit('Post','Post',css_class='btn-primary'))
  class Meta:
     model = Post
     fields =[
       'image',
       'caption'
     ]

class UserPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author', 'posted_date','comments','likes']
       
