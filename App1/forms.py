from django.forms import ModelForm
from .models import Blog
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Newpost(ModelForm):

	class Meta:
		model=Blog
		fields=['title','caption','photo1','photo2','blog']
		
		def __init__(self, *args, **kwargs):
			super(Newpost, self).__init__(*args, **kwargs)
			self.fields['blog'].widget.attrs.update({'autocomplete':'off'})
			self.fields['caption'].widget.attrs.update({'autocomplete':'off'})
			self.fields['title'].widget.attrs.update({'autocomplete':'off'})
			
class UserCreationFormUpdate(UserCreationForm):
	class Meta:
		model=User
		fields=['username','email','password1','password2']
