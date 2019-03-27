from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import NewPostForm, NewCommentForm, Profileform
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from .models import Image, Profile, Comment, Follow, Likes
from django.contrib.auth import authenticate, login 
from actstream.actions import follow, unfollow
from actstream.models import following, followers


@login_required(login_url='/accounts/register/')
def home(request):
     title='Home | instaphoto'
     current_user=request.user
     profile=Profile.objects.get(user=current_user)
     following1=following(request.user)
     posts=Image.objects.all()
    
     return render(request,'instapic/index.html',{'title':title , 'posts':posts, 'following':following1})

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def post(request,id):
    post=Image.objects.get(id=id)
    number_of_likes = Likes.objects.filter(image=post).count()

    comments=Comment.objects.filter(image=post)
    return render(request, 'instapic/post.html', {"post": post, 'comments':comments, 'likes':number_of_likes})

@login_required(login_url='/accounts/login/')
def like_home(request,picture_id):
    post=Image.objects.get(id=picture_id)
    new_like, created = Likes.objects.get_or_create(user=request.user, image_id=picture_id)
    number_of_likes = Likes.objects.filter(image=post).count()
    post.likess=number_of_likes
    post.save()
    if not created:
        message='U already liked the picture'
    else:
        message='like successful'
    return redirect('home')
@login_required(login_url='/accounts/login/')
def like_post(request, picture_id):
    post=Image.objects.get(id=picture_id)
    new_like, created = Likes.objects.get_or_create(user=request.user, image_id=picture_id)
    if not created:
        message='U already liked the picture'
    else:
        message='like successful'
    return redirect('post',post.id)


@login_required(login_url='/accounts/login/')
def add_comment(request,id):
        current_user = request.user
        post=Image.objects.get(id=id)
        if request.method == 'POST':
               form = NewCommentForm(request.POST)
               if form.is_valid():
                    comment= form.cleaned_data['comment']
                   
                    new_comment = Comment(comment = comment,user =current_user,image=post)
                    new_comment.save()
                    
                    HttpResponseRedirect('home')
        else:
                    form = NewCommentForm()
        return render(request, 'instapic/new_comment.html', {"letterForm":form,'post':post,'user':current_user})
@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_users = search_by_username(search_term)
        message =f"{search_term}"

        return render(request, 'instapic/search.html',{"message":message,"users": searched_users})

    else:
        message = "You haven't searched for any term"
        return render(request, 'grams/search.html',{"message":message})

     

def search_by_username(name):
       users=User.objects.filter(username__icontains=name)
       return users
@login_required(login_url='/accounts/login/')
def profile(request,id):
     user=User.objects.get(id=id)
     profile=Profile.objects.get(user=user)
     images=Image.objects.filter(user=user)
    #  following=following(user)
    #  followers1=followers(profile)
    
     return render(request, 'instapic/profile.html',{"user":user,"profile": profile, 'images':images})
     
@login_required(login_url='/accounts/login/')
def edit_profile(request,edit):
    current_user = request.user
    profile=Profile.objects.get(user=current_user)
    
   
    if request.method == 'POST':
        form = Profileform(request.POST, request.FILES)
        if form.is_valid():
            
            profile.bio=form.cleaned_data['bio']
            profile.photo = form.cleaned_data['photo']
            profile.user=current_user
            
            profile.save()
        return redirect('home')

    else:
        form = Profileform()
    return render(request, 'edit_profile.html', {"form": form , 'user':current_user})


@login_required(login_url='/accounts/login/')
def follow_profile(request,id):
    profile=Profile.objects.get(id=id)
    follow(request.user,profile)
    return redirect('index')

@login_required(login_url='/accounts/login/')
def unfollow_profile(request,id):
    profile=Profile.objects.get(id=id)
    unfollow(request.user,profile)
    return redirect('index')


@login_required(login_url='/accounts/login/')
def who_following(request,id):
    user=User.objects.get(id=id)
    following1=following(user)
    return render(request, 'following.html', {'user':request.user, 'following':following1})


@login_required(login_url='/accounts/login/')
def who_followers(request,id):
    user=Profile.objects.get(id=id)
    following1=followers(user)
    return render(request, 'followers.html', {'user':request.user, 'following':following1})