from .models import Image, Profile
from django import forms

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user','profile', 'pub_date']


class Profileform(forms.ModelForm):
     class Meta:
         model= Profile
         exclude = ['user']

   

    