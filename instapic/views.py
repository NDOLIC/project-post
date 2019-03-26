# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http  import HttpResponse
from .forms import NewPostForm
# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to Instagram')


def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            likes=Likes(likes=0,liked=False,user=current_user)
            likes.save()
            post.likes=likes
            
            post.save()
        return redirect('home')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})