from .models import Image, Profile
from django import forms

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user','profile', 'pub_date','likess','follow']

class NewCommentForm(forms.Form):
    comment = forms.CharField(label='Comment',max_length=600)

class Profileform(forms.ModelForm):
     class Meta:
         model= Profile
         exclude = ['user']

   

    