from django import forms
from django.contrib.auth import (
  authenticate,
  get_user_model
  )
User = get_user_model()

class UserLoginForm(forms.Form):
  username= forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput)
  def clean(self,*args,**kwargs):
    username= self.cleaned_data.get('username')
    password = self.cleaned_data.get('password')
    if username and password:
      user= authenticate(username =username,password=password)
      if not user:
        raise forms.ValidationError("Username does not exist")
      if not user.check_password(password):
        raise forms.ValidationError("Incorrect password")
      if not user.is_active:
        raise forms.ValidationError('This User is not logged in')
      return super(UserLoginForm,self).clean(*args,**kwargs)
class UserRegisterForm(forms.ModelForm):
  email= forms.EmailField(label='Email')
  emailb = forms.EmailField(label='confirm email')
  name = forms.TextInput()
  password = forms.CharField(widget=forms.PasswordInput)

  class Meta:
    model= User
    fields = [
      'username',
      'email',
      'emailb',
      
      'password',
    ]

    def clean(self,*args,**kwargs):
      email = self.cleaned_data.get('email')
      emailb = self.cleaned_data.get('emailb')
      if email!= emailb:
        raise forms.ValidationError('Emails do not match')
      email_qs = User.objects.filter(email=email)
      if email_qs.exists():
          raise forms.ValidationError("This email is already associated with an account")
      return super(UserRegisterForm,self).clean(*args,**kwargs)


