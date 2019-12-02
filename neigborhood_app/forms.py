from django import forms
from .models import *


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']
        
class PostUpload(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','post')