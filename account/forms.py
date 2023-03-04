from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
  password = forms.CharField(label='Password', widget=forms.PasswordInput)
  password2 = forms.CharField(label='Re-enter your password', widget=forms.PasswordInput)

  class Meta:
    fields = ('first_name', 'username', 'email')
    model = User

  def clean_password2(self):
    cd = self.cleaned_data
    if cd['password2'] != cd['password']:
      raise forms.ValidationError('The passwords you entered don\'t match')
    return cd['password2']
