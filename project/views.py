from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import NewPostForm, Profileform
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from .models import Image, Profile
from django.contrib.auth import authenticate, login 
from django.http import JsonResponse
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer



@login_required(login_url='/accounts/register/')
def home(request):
     title='Home | projectpost'
     current_user=request.user
     profile=Profile.objects.get(user=current_user)
     posts=Image.objects.all()
    
     return render(request,'project/index.html',{'title':title , 'posts':posts})

class ProfileList(APIView):
    def get (self,request):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile,many=True)
        return Response(serializer.data)

    def post(self):
        pass

class ProjectList(APIView):
    def get(self,request):
        project = Project.objects.all()
        serializer=ProjectSerializer(project,many=True)
        return Response(serializer.data)

    def post(self):
        pass

